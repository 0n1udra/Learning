import threading, os
from queue import Queue
from urllib.request import urlopen
from html.parser import HTMLParser
# Link finder############################################################################################################################################################
class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_Links(self):
        return self.links
    def error(self, message): pass
# File editing part############################################################################################################################################################
def create_Directory(directory): # creates new folders for projects
    if not os.path.exists(directory): # checks if folder already exists
        print("Creating dir > " + directory)
        os.makedirs(directory)
# creates queue file and crawled file
def create_File(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue): write_to_File(queue, base_url)
    if not os.path.isfile(crawled): write_to_File(crawled, '')
# make file
def write_to_File(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
# add data to existing file
def append_to_File(path, data):
    with open(path, 'a') as file: file.write(data + '\n')
# clear file data
def delete_file_Data(path):
    with open(path, 'w'): pass
# read file, convert to item, put into set
def filedata_to_Set(filename):
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results
# iterate thorugh 'results' each item is a new file
def set_to_File(links, file):
    delete_file_Data(file)
    for link in sorted(links): append_to_File(file, link)
# Spider ############################################################################################################################################################
class Spider:
    project_name, base_url, domain_name = '', '', ''
    queue_file, crawled_file = '', ''
    queue, crawled = set(), set()

    def __init__(self, project_name, base_url, domian_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domian_name

        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'

        self.boot()
        self.crawl_Page("First Spider" , Spider.base_url)

    @staticmethod
    def boot():
        create_Directory(Spider.project_name)
        create_File(Spider.project_name, Spider.base_url)
        Spider.queue = filedata_to_Set(Spider.queue_file)
        Spider.crawled = filedata_to_Set(Spider.crawled_file)

    @staticmethod
    def crawl_Page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name +  " :Crawling: " + page_url)
            print("Queue " + str(len(Spider.queue)) + " | Crawled   " + str(len(Spider.crawled)))
            Spider.add_links_to_Queue(Spider.gather_Links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_Files()

    @staticmethod
    def gather_Links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader("Content-Type") == "text/html":
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print("ERROR: not able to craw page")
            return set()
        return finder.page_Links()

    @staticmethod
    def add_links_to_Queue(links):
        for url in links:
            if url in Spider.queue: continue
            if url in Spider.crawled: continue
            if Spider.domain_name not in url: continue
            Spider.queue.add(url)

    @staticmethod
    def update_Files():
        set_to_File(Spider.queue, Spider.queue_file)
        set_to_File(Spider.crawled, Spider.crawled_file)

# get's sub-domain name############################################################################################################################################################
def get_domain_name(url):
    try:
        result = get_sub_domain_name(url).spit('.')
        return result[-2] + '.' + result[-1]
    except:
        return ''
#get sub-domain
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
# Main, runs############################################################################################################################################################

PROJECT_NAME = "theVerge"
HOMEPAGE = "http://www.theverge.com/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 2
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
# create worker threads (will die in main dies)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
# does next job in queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_Page(threading.current_thread().name, url)
        queue.task_done()
# each link in queue is a job
def create_job():
    for link in filedata_to_Set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()
# checks for itmes in queue
def crawl():
    queued_links = filedata_to_Set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links + "many links in queue")))
        create_jobs()

create_workers()
crawl()
