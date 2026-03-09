#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PhantomSubfinder v2.0 - The Ultimate Reconnaissance Tool
# By Illusivehacks - Upgraded with GOD-TIER features! 👻

import os
import sys
import time
import subprocess
import platform
import re
import json
import socket
import threading
import random
import urllib.request
import urllib.error
import urllib.parse
import ssl
import dns.resolver
import dns.reversename
import dns.exception
import requests
import hashlib
import base64
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
from datetime import datetime
from colorama import init, Fore, Back, Style
from urllib.parse import urlparse
import queue
import argparse
import warnings
import logging

# Suppress all warnings and disable SSL warnings
warnings.filterwarnings("ignore")
logging.captureWarnings(True)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("requests").setLevel(logging.ERROR)

# Disable SSL warnings completely
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

# Initialize colorama for cross-platform colors
init(autoreset=True)

# Phantom Colors - Enhanced Edition
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    END = '\033[0m'
    
    # Emoji shortcuts
    GHOST = '👻'
    SKULL = '💀'
    FIRE = '🔥'
    CLOUD = '☁️'
    LOCK = '🔒'
    UNLOCK = '🔓'
    WARNING = '⚠️'
    INFO = 'ℹ️'
    SUCCESS = '✅'
    ERROR = '❌'
    TIME = '⏱️'
    NETWORK = '🌐'
    DATABASE = '🗄️'
    WEB = '🌍'
    EMAIL = '📧'
    SERVER = '🖥️'
    MOBILE = '📱'
    ALERT = '🚨'
    BUG = '🐛'
    EYE = '👁️'
    MAP = '🗺️'
    CROWN = '👑'

# Auto-setup with enhanced package management
def phantom_auto_setup():
    """Phantom automatically installs all requirements with version checking"""
    
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    required_packages = {
        'requests': '2.25.0',
        'dnspython': '2.1.0',
        'colorama': '0.4.4',
        'beautifulsoup4': '4.9.3',
        'lxml': '4.6.3',
        'cryptography': '3.4.7',
        'urllib3': '1.26.5'
    }
    
    python_cmd = sys.executable
    
    print(f"{Colors.PURPLE}╔══════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.PURPLE}║{Colors.CYAN}          PHANTOM SUBFINDER V2.0 - AUTO SETUP            {Colors.PURPLE}{Colors.END}")
    print(f"{Colors.PURPLE}║{Colors.GREEN}                    By Illusivehacks & Wilshewz                     {Colors.PURPLE}{Colors.END}")
    print(f"{Colors.PURPLE}╚══════════════════════════════════════════════════════════════╝{Colors.END}\n")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print(f"{Colors.RED}[{Colors.ERROR}] Error: Python 3.7+ required (found {sys.version_info[0]}.{sys.version_info[1]}){Colors.END}")
        sys.exit(1)
    
    print(f"{Colors.GREEN}[{Colors.SUCCESS}] Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} detected{Colors.END}\n")
    
    # Install/Update required packages
    for package, min_version in required_packages.items():
        print(f"{Colors.CYAN}[*] Checking {package}...{Colors.END}", end='', flush=True)
        try:
            if package == 'dnspython':
                import dns
                module = dns
            else:
                module = __import__(package)
            
            # Version checking logic
            if hasattr(module, '__version__'):
                version = module.__version__
            else:
                version = "unknown"
            
            print(f"\r{Colors.GREEN}[{Colors.SUCCESS}] {package} {version} found    {Colors.END}")
        except (ImportError, AttributeError):
            print(f"\r{Colors.YELLOW}[{Colors.WARNING}] {package} not found/outdated. Installing...{Colors.END}")
            try:
                subprocess.check_call([python_cmd, "-m", "pip", "install", "--quiet", "--upgrade", package])
                print(f"\r{Colors.GREEN}[{Colors.SUCCESS}] {package} installed successfully{Colors.END}")
            except subprocess.CalledProcessError:
                print(f"\r{Colors.RED}[{Colors.ERROR}] Failed to install {package}{Colors.END}")
                sys.exit(1)
    
    # Create enhanced wordlists
    create_enhanced_wordlists()
    
    print(f"\n{Colors.GREEN}[{Colors.SUCCESS}] Phantom setup complete! Ready to hunt.{Colors.END}\n")
    time.sleep(2)

def create_enhanced_wordlists():
    """Create comprehensive subdomain wordlists with categories"""
    base_dir = os.path.join(os.path.dirname(__file__), 'wordlists')
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Common subdomains wordlist
    common_path = os.path.join(base_dir, 'common.txt')
    if not os.path.exists(common_path):
        print(f"{Colors.CYAN}[*] Generating common subdomain wordlist...{Colors.END}")
        
        common_subs = [
            # Web Services
            'www', 'ww2', 'ww3', 'web', 'website', 'site', 'home', 'index',
            'default', 'main', 'portal', 'gateway', 'gate', 'access',
            
            # Email Services
            'mail', 'email', 'webmail', 'smtp', 'pop', 'imap', 'exchange',
            'outlook', 'office365', 'mail1', 'mail2', 'mail3', 'mx',
            
            # DNS Services
            'ns1', 'ns2', 'ns3', 'ns4', 'dns', 'dns1', 'dns2', 'resolver',
            
            # Administrative
            'admin', 'administrator', 'admin1', 'admin2', 'adm', 'manage',
            'management', 'manager', 'control', 'cpanel', 'whm', 'webmin',
            
            # Development
            'dev', 'develop', 'development', 'stage', 'staging', 'test',
            'testing', 'qa', 'uat', 'sandbox', 'sand', 'box', 'playground',
            'lab', 'labs', 'demo', 'demos', 'beta', 'alpha', 'rc', 'release',
            
            # API Services
            'api', 'api1', 'api2', 'api3', 'rest', 'restapi', 'graphql',
            'graph', 'gql', 'swagger', 'apidocs', 'docs-api', 'developer',
            
            # Security
            'security', 'secure', 'safe', 'protect', 'protection', 'waf',
            'firewall', 'fw', 'ids', 'ips', 'siem', 'soc', 'cert', 'ca',
            'ssl', 'tls', 'vpn', 'vpn1', 'vpn2', 'remote-access',
            
            # Cloud Services
            'cloud', 'aws', 'azure', 'gcp', 'google-cloud', 'amazon',
            's3', 'bucket', 'storage', 'blob', 'container', 'registry',
            
            # Monitoring
            'monitor', 'monitoring', 'status', 'health', 'uptime', 'ping',
            'stats', 'statistics', 'metrics', 'grafana', 'prometheus',
            
            # Databases
            'db', 'database', 'mysql', 'postgres', 'postgresql', 'mongo',
            'mongodb', 'redis', 'elastic', 'elasticsearch', 'cassandra',
            
            # Version Control
            'git', 'github', 'gitlab', 'bitbucket', 'svn', 'version',
            'repo', 'repository', 'source', 'code', 'src',
            
            # CI/CD
            'ci', 'cd', 'jenkins', 'travis', 'circleci', 'build', 'builder',
            'artifact', 'artifacts', 'nexus', 'jfrog', 'docker',
            
            # Communication
            'chat', 'talk', 'message', 'messages', 'notification', 'alert',
            'webhook', 'callback', 'webchat', 'livechat', 'support',
            
            # Files & Media
            'files', 'file', 'upload', 'uploads', 'download', 'downloads',
            'media', 'images', 'img', 'css', 'js', 'static', 'assets',
            
            # Business
            'shop', 'store', 'cart', 'checkout', 'payment', 'billing',
            'invoice', 'orders', 'customer', 'customers', 'client', 'clients',
            
            # Old Versions
            'old', 'new', 'temp', 'tmp', 'backup', 'backups', 'archive',
            'archives', 'legacy', 'migration', 'migrated', 'deprecated'
        ]
        
        with open(common_path, 'w') as f:
            for sub in common_subs:
                f.write(sub + '\n')
        
        print(f"{Colors.GREEN}[{Colors.SUCCESS}] Common wordlist created with {len(common_subs)} entries{Colors.END}")
    
    # Heavy wordlist for intensive bruteforce
    heavy_path = os.path.join(base_dir, 'heavy.txt')
    if not os.path.exists(heavy_path):
        print(f"{Colors.CYAN}[*] Generating heavy wordlist (this may take a moment)...{Colors.END}")
        
        # Generate variations
        heavy_subs = []
        base_words = ['admin', 'api', 'dev', 'test', 'mail', 'web', 'cloud', 'secure']
        
        # Add number variations
        for word in base_words:
            heavy_subs.append(word)
            for i in range(1, 100):
                heavy_subs.append(f"{word}{i}")
                heavy_subs.append(f"{word}-{i}")
        
        # Add common patterns
        patterns = ['dev-', 'test-', 'stage-', 'prod-', 'uat-', 'qa-']
        for pattern in patterns:
            for word in ['server', 'app', 'web', 'api', 'db', 'cache']:
                heavy_subs.append(f"{pattern}{word}")
                heavy_subs.append(f"{word}{pattern}")
        
        # Remove duplicates and sort
        heavy_subs = sorted(set(heavy_subs))
        
        with open(heavy_path, 'w') as f:
            for sub in heavy_subs:
                f.write(sub + '\n')
        
        print(f"{Colors.GREEN}[{Colors.SUCCESS}] Heavy wordlist created with {len(heavy_subs)} entries{Colors.END}")

class EnhancedPhantomSubfinder:
    def __init__(self):
        self.domain = ""
        self.subdomains = set()
        self.live_subdomains = {}
        self.resolved_ips = {}
        self.ports_open = {}
        self.tech_stack = {}
        self.cloud_assets = {
            's3': set(),
            'azure': set(),
            'gcp': set(),
            'custom': set()
        }
        self.dependency_graph = {}
        self.results_db = {}
        self.wordlist_paths = {
            'common': os.path.join(os.path.dirname(__file__), 'wordlists', 'common.txt'),
            'heavy': os.path.join(os.path.dirname(__file__), 'wordlists', 'heavy.txt')
        }
        
        # Configuration
        self.timeout = 5
        self.threads = 50
        self.delay = 0
        self.stealth_mode = False
        self.user_agents = self.generate_user_agents()
        self.proxies = []
        self.current_proxy = None
        
        # Initialize DNS resolver
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ['8.8.8.8', '8.8.4.4', '1.1.1.1', '9.9.9.9']
        self.resolver.timeout = self.timeout
        self.resolver.lifetime = self.timeout
        
        # Thread pools
        self.executor = ThreadPoolExecutor(max_workers=self.threads)
        self.task_queue = queue.Queue()
        
        # Statistics
        self.stats = {
            'start_time': None,
            'queries': 0,
            'found': 0,
            'errors': 0
        }
        
        self.banner()

    def generate_user_agents(self):
        """Generate 100+ unique user agents from the TikTok pattern"""
        user_agents = []
        browsers = ['Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', 'Brave', 'Vivaldi']
        platforms = ['Windows NT 10.0; Win64; x64', 'Windows NT 6.1; Win64; x64', 
                    'Macintosh; Intel Mac OS X 10_15_7', 'Macintosh; Intel Mac OS X 11_2_3',
                    'X11; Linux x86_64', 'X11; Ubuntu; Linux x86_64']
        
        for _ in range(150):  # Generate 150 unique UAs
            browser = random.choice(browsers)
            platform = random.choice(platforms)
            
            if browser == 'Chrome':
                version = f"{random.randint(90, 120)}.0.{random.randint(4000, 5000)}.{random.randint(100, 200)}"
                webkit = f"537.36 (KHTML, like Gecko)"
                ua = f"Mozilla/5.0 ({platform}) AppleWebKit/{webkit} {browser}/{version} Safari/{webkit}"
            elif browser == 'Firefox':
                version = f"{random.randint(80, 110)}.0"
                ua = f"Mozilla/5.0 ({platform}; rv:{version}) Gecko/20100101 {browser}/{version}"
            elif browser == 'Safari':
                version = f"{random.randint(600, 700)}.{random.randint(1, 20)}.{random.randint(1, 50)}"
                ua = f"Mozilla/5.0 ({platform}) AppleWebKit/{version} (KHTML, like Gecko) Version/{random.randint(14, 16)}.{random.randint(0, 3)} Safari/{version}"
            else:
                ua = f"Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{random.randint(80, 100)}.0.{random.randint(1000, 5000)} Safari/537.36"
            
            user_agents.append(ua)
        
        return list(set(user_agents))  # Remove duplicates
    
    def get_random_user_agent(self):
        """Get a random user agent from the pool"""
        return random.choice(self.user_agents)

    def banner(self):
        """Display the enhanced Phantom banner"""
        os.system('cls' if os.name == 'nt' else 'clear')
        banner_text = f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     █████▄ ▄▄ ▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄▄▄▄▄ ▄▄▄  ▄▄   ▄▄    {Colors.CYAN}PHANTOM V2.0{Colors.PURPLE}      
║     ██▄▄█▀ ██▄██ ██▀██ ███▄██   ██  ██▀██ ██▀▄▀██    {Colors.GREEN}ULTIMATE{Colors.PURPLE}         
║     ██     ██ ██ ██▀██ ██ ▀██   ██  ▀███▀ ██   ██    {Colors.YELLOW}RECON{Colors.PURPLE}            
║                                                                              
║         ▄█████ ▄▄ ▄▄ ▄▄▄▄  ██████ ▄▄ ▄▄  ▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄              
║         ▀▀▀▄▄▄ ██ ██ ██▄██ ██▄▄   ██ ███▄██ ██▀██ ██▄▄  ██▄█▄              
║         █████▀ ▀███▀ ██▄█▀ ██     ██ ██ ▀██ ████▀ ██▄▄▄ ██ ██              
║                                                                              
║{Colors.GREEN}              👻 PHANTOM SUBFINDER - RECON 👻{Colors.PURPLE}                    
║{Colors.CYAN}                    By Illusivehacks & Wilshewz{Colors.PURPLE}                                          
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.YELLOW}  Multi-Threaded | Cloud Enum | Port Scan | Tech Detect | Stealth{Colors.PURPLE}    
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}
"""
        print(banner_text)

    def print_enhanced_help(self):
        """Display enhanced help menu with all new features"""
        help_text = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║                       PHANTOM V2.0 - ULTIMATE COMMANDS                        
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              
║  {Colors.YELLOW}CORE COMMANDS:{Colors.CYAN}                                                          
║  ────────────────────────────────────────────────────────────────────────────║
║  {Colors.GREEN}hunt{Colors.CYAN} <domain>              Passive OSINT enumeration (crt.sh, VT, etc)   
║  {Colors.GREEN}bruteforce{Colors.CYAN} <domain>        Multi-threaded DNS bruteforce                 
║  {Colors.GREEN}full-recon{Colors.CYAN} <domain>        ALL-IN-ONE: Hunt + Bruteforce + Scan       
║                                                                              
║  {Colors.YELLOW}NEW FEATURES:{Colors.CYAN}                                                        
║  ────────────────────────────────────────────────────────────────────────────║
║  {Colors.GREEN}bruteforce{Colors.CYAN} <domain> --threads <num>   Set thread count (default: 50)    
║  {Colors.GREEN}bruteforce{Colors.CYAN} <domain> --wordlist <file> Use custom wordlist                
║                                                                              
║  {Colors.GREEN}scan{Colors.CYAN} <domain> --live            Live host validation + HTTP probing       
║  {Colors.GREEN}scan{Colors.CYAN} <domain> --ports <range>    Port scan + service detection            
║     Examples: --ports 80,443,8080    --top-ports 1000    --ports 1-1000    
║                                                                              
║  {Colors.GREEN}recurse{Colors.CYAN} <domain> --depth <n>    Recursive subdomain enumeration           
║  {Colors.GREEN}cloud{Colors.CYAN} <domain>               Cloud asset enumeration (S3, Azure, GCP)    
║                                                                              
║  {Colors.GREEN}map{Colors.CYAN} <domain>                 Build dependency graph + tech stack         
║  {Colors.GREEN}stealth{Colors.CYAN} <domain>             Stealth mode with delays & random UAs       
║                                                                              
║  {Colors.YELLOW}EXAMPLES:{Colors.CYAN}                                                            
║  ────────────────────────────────────────────────────────────────────────────║
║  {Colors.DIM}$ phantom@subfinder → bruteforce github.com --threads 100 --wordlist heavy.txt{Colors.CYAN}    
║  {Colors.DIM}$ phantom@subfinder → scan github.com --live --ports 80,443,8080{Colors.CYAN}                
║  {Colors.DIM}$ phantom@subfinder → recurse github.com --depth 3{Colors.CYAN}                                 
║  {Colors.DIM}$ phantom@subfinder → cloud github.com{Colors.CYAN}                                             
║  {Colors.DIM}$ phantom@subfinder → full-recon github.com --output report.html{Colors.CYAN}                   
║                                                                              
║  {Colors.YELLOW}OTHER COMMANDS:{Colors.CYAN}                                                      
║  ────────────────────────────────────────────────────────────────────────────║
║  export <filename>     Export results to file (JSON/HTML/TXT)               
║  clear                 Clear the screen                                     
║  help                  Show this help menu                                   
║  exit                  Exit Phantom Subfinder                                
║                                                                              
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}
"""
        print(help_text)

    # ==================== UPGRADE 1: MULTI-THREADED BRUTEFORCE ENGINE ====================
    def enhanced_bruteforce(self, domain, threads=50, wordlist='common', custom_wordlist=None):
        """Multi-threaded bruteforce with configurable thread count"""
        print(f"\n{Colors.YELLOW}[{Colors.FIRE}] Starting enhanced multi-threaded brute force...{Colors.END}")
        print(f"{Colors.CYAN}[{Colors.INFO}] Threads: {threads} | Wordlist: {wordlist}{Colors.END}")
        
        subdomains = set()
        
        # Determine wordlist path
        if custom_wordlist and os.path.exists(custom_wordlist):
            wordlist_path = custom_wordlist
        else:
            wordlist_path = self.wordlist_paths.get(wordlist, self.wordlist_paths['common'])
        
        if not os.path.exists(wordlist_path):
            print(f"{Colors.RED}[{Colors.ERROR}] Wordlist not found: {wordlist_path}{Colors.END}")
            return subdomains
        
        # Load wordlist
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                words = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"{Colors.RED}[{Colors.ERROR}] Failed to load wordlist: {e}{Colors.END}")
            return subdomains
        
        total = len(words)
        found = 0
        lock = threading.Lock()
        
        print(f"{Colors.CYAN}[{Colors.INFO}] Loaded {total} words. Starting resolution...{Colors.END}")
        
        def check_sub(word):
            nonlocal found
            subdomain = f"{word}.{domain}"
            
            # Add stealth delay if enabled
            if self.stealth_mode:
                time.sleep(random.uniform(0.1, 0.5))
            
            try:
                # Try DNS resolution
                answers = self.resolver.resolve(subdomain, 'A')
                if answers:
                    ips = [str(rdata) for rdata in answers]
                    with lock:
                        subdomains.add(subdomain)
                        self.resolved_ips[subdomain] = ips
                        found += 1
                        print(f"{Colors.GREEN}[{Colors.SUCCESS}] Found: {subdomain} ({found}/{total}) - IPs: {', '.join(ips[:3])}{Colors.END}")
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
                pass
            except Exception as e:
                with lock:
                    self.stats['errors'] += 1
        
        # Multi-threaded execution
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=threads) as executor:
            list(executor.map(check_sub, words))
        
        elapsed = time.time() - start_time
        print(f"\n{Colors.GREEN}[{Colors.SUCCESS}] Brute force complete! Found {len(subdomains)} subdomains in {elapsed:.2f} seconds{Colors.END}")
        print(f"{Colors.CYAN}[{Colors.INFO}] Average speed: {total/elapsed:.0f} queries/second{Colors.END}")
        
        return subdomains

    # ==================== UPGRADE 2: LIVE HOST VALIDATION + HTTP PROBING ====================
    def live_host_validation(self, subdomains, http_probe=True):
        """Validate live hosts and perform HTTP probing"""
        print(f"\n{Colors.YELLOW}[{Colors.NETWORK}] Validating live hosts...{Colors.END}")
        
        live_hosts = {}
        tech_detected = {}
        
        def validate_host(subdomain):
            try:
                # DNS resolution first
                answers = self.resolver.resolve(subdomain, 'A')
                if not answers:
                    return None
                
                ips = [str(rdata) for rdata in answers]
                
                # HTTP probing
                if http_probe:
                    for protocol in ['https', 'http']:
                        try:
                            url = f"{protocol}://{subdomain}"
                            
                            # Use random user agent
                            headers = {
                                'User-Agent': self.get_random_user_agent(),
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'Accept-Language': 'en-US,en;q=0.5',
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'keep-alive',
                                'Upgrade-Insecure-Requests': '1'
                            }
                            
                            # Add stealth delay
                            if self.stealth_mode:
                                time.sleep(random.uniform(1, 3))
                            
                            response = requests.get(
                                url, 
                                headers=headers,
                                timeout=self.timeout,
                                verify=False,
                                allow_redirects=True
                            )
                            
                            # Extract technology stack
                            tech = self.detect_technology(response)
                            
                            result = {
                                'ip': ips,
                                'status_code': response.status_code,
                                'title': self.extract_title(response.text),
                                'server': response.headers.get('Server', 'Unknown'),
                                'tech': tech,
                                'url': response.url,
                                'redirects': len(response.history)
                            }
                            
                            print(f"{Colors.GREEN}[{Colors.SUCCESS}] {subdomain} [{response.status_code}] Title: \"{result['title']}\" | Server: {result['server']}{Colors.END}")
                            return subdomain, result
                            
                        except requests.exceptions.RequestException:
                            continue
                
                # If HTTP probe failed or disabled, still mark as live
                return subdomain, {'ip': ips, 'alive': True}
                
            except Exception:
                return None
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(validate_host, sub): sub for sub in subdomains}
            for future in as_completed(futures):
                result = future.result()
                if result:
                    sub, info = result
                    live_hosts[sub] = info
                    if 'tech' in info:
                        tech_detected[sub] = info['tech']
        
        self.live_subdomains = live_hosts
        self.tech_stack.update(tech_detected)
        
        print(f"\n{Colors.GREEN}[{Colors.SUCCESS}] Validation complete! {len(live_hosts)} live hosts found{Colors.END}")
        return live_hosts

    def extract_title(self, html):
        """Extract page title from HTML"""
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            return title[:50] + '...' if len(title) > 50 else title
        return 'No Title'

    def detect_technology(self, response):
        """Detect technology stack from response"""
        tech = []
        headers = response.headers
        html = response.text.lower()
        
        # Server header
        if 'Server' in headers:
            tech.append(f"Server: {headers['Server']}")
        
        # Framework detection
        if 'x-powered-by' in headers:
            tech.append(f"Powered by: {headers['x-powered-by']}")
        
        # CMS Detection
        if 'wp-content' in html or 'wordpress' in html:
            tech.append('WordPress')
        if 'drupal' in html:
            tech.append('Drupal')
        if 'joomla' in html:
            tech.append('Joomla')
        if 'shopify' in html or 'myshopify' in html:
            tech.append('Shopify')
        
        # JavaScript frameworks
        if 'react' in html or 'reactjs' in html:
            tech.append('React')
        if 'angular' in html:
            tech.append('Angular')
        if 'vue' in html:
            tech.append('Vue.js')
        
        # Cloud providers
        if 'cloudfront' in html:
            tech.append('AWS CloudFront')
        if 'azure' in html:
            tech.append('Azure')
        
        return list(set(tech))

    # ==================== UPGRADE 3: RECURSIVE SUBDOMAIN ENUMERATION ====================
    def recursive_hunt(self, domain, depth=2, current_depth=1):
        """Recursively hunt for subdomains of subdomains"""
        if current_depth > depth:
            return set()
        
        print(f"\n{Colors.YELLOW}[{Colors.MAP}] Recursive hunt level {current_depth}/{depth} for {domain}{Colors.END}")
        
        # Get subdomains at current level
        found = self.hunt(domain, quiet=True)
        
        if current_depth < depth:
            # For each found subdomain, hunt recursively
            for sub in list(found)[:10]:  # Limit to 10 to avoid explosion
                sub_without_domain = sub.replace(f".{domain}", "")
                if '.' in sub_without_domain:  # Has sub-subdomain
                    deeper = self.recursive_hunt(sub, depth, current_depth + 1)
                    found.update(deeper)
        
        return found

    # ==================== UPGRADE 4: SMART PORT SCANNING + SERVICE DETECTION ====================
    def enhanced_port_scan(self, subdomains, ports=None, top_ports=100):
        """Port scanning with service detection"""
        print(f"\n{Colors.YELLOW}[{Colors.SERVER}] Starting enhanced port scan...{Colors.END}")
        
        # Common ports and their services
        common_ports = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 110: 'POP3', 111: 'RPC', 135: 'RPC', 139: 'NetBIOS',
            143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
            1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
            5900: 'VNC', 5985: 'WinRM', 5986: 'WinRM', 6379: 'Redis',
            8080: 'HTTP-Alt', 8443: 'HTTPS-Alt', 27017: 'MongoDB'
        }
        
        if ports is None:
            # Use top ports
            ports = list(common_ports.keys())[:top_ports]
        
        results = {}
        
        def scan_host_port(host, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((host, port))
                
                if result == 0:
                    # Try to grab banner
                    try:
                        sock.send(b'\r\n')
                        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                    except:
                        banner = None
                    
                    service = common_ports.get(port, 'Unknown')
                    
                    # Service detection from banner
                    if banner:
                        if 'SSH' in banner:
                            service = f"SSH: {banner.split()[0]}"
                        elif 'HTTP' in banner:
                            service = f"HTTP: {banner.split()[0]}"
                    
                    print(f"{Colors.GREEN}[+] {host}:{port} - OPEN ({service}){Colors.END}")
                    if banner:
                        print(f"{Colors.DIM}    Banner: {banner[:50]}{Colors.END}")
                    
                    return port, {'service': service, 'banner': banner}
                
                sock.close()
            except:
                pass
            return None
        
        for host in subdomains:
            host_results = {}
            print(f"\n{Colors.CYAN}[*] Scanning {host}...{Colors.END}")
            
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = {executor.submit(scan_host_port, host, port): port for port in ports}
                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        port, info = result
                        host_results[port] = info
            
            if host_results:
                results[host] = host_results
                self.ports_open[host] = host_results
        
        return results

    # ==================== UPGRADE 5: CLOUD ENUMERATION MODULE ====================
    def enumerate_cloud_assets(self, domain):
        """Enumerate cloud assets like S3 buckets, Azure blobs, GCP buckets"""
        print(f"\n{Colors.YELLOW}[{Colors.CLOUD}] Enumerating cloud assets for {domain}...{Colors.END}")
        
        cloud_assets = {
            's3': [],
            'azure': [],
            'gcp': [],
            'custom': []
        }
        
        # Common bucket naming patterns
        base_name = domain.replace('.', '-')
        patterns = [
            base_name,
            f"{base_name}-assets",
            f"{base_name}-static",
            f"{base_name}-media",
            f"{base_name}-public",
            f"{base_name}-private",
            f"{base_name}-dev",
            f"{base_name}-prod",
            f"dev-{base_name}",
            f"prod-{base_name}",
            f"assets.{domain}",
            f"static.{domain}",
            f"media.{domain}",
            f"cdn.{domain}"
        ]
        
        def check_s3_bucket(bucket_name):
            """Check if S3 bucket exists and is accessible"""
            url = f"http://{bucket_name}.s3.amazonaws.com"
            try:
                response = requests.get(url, timeout=5, verify=False)
                if response.status_code != 404:
                    info = {
                        'name': bucket_name,
                        'url': url,
                        'accessible': response.status_code == 200,
                        'public': response.status_code not in [403, 401]
                    }
                    cloud_assets['s3'].append(info)
                    status = "PUBLIC" if info['public'] else "PRIVATE"
                    print(f"{Colors.GREEN}[{Colors.CLOUD}] S3: {bucket_name} ({status}){Colors.END}")
            except:
                pass
        
        def check_azure_blob(blob_name):
            """Check if Azure blob exists"""
            url = f"http://{blob_name}.blob.core.windows.net"
            try:
                response = requests.get(url, timeout=5, verify=False)
                if response.status_code != 404:
                    info = {
                        'name': blob_name,
                        'url': url,
                        'accessible': response.status_code == 200
                    }
                    cloud_assets['azure'].append(info)
                    print(f"{Colors.GREEN}[{Colors.CLOUD}] Azure: {blob_name}{Colors.END}")
            except:
                pass
        
        def check_gcp_bucket(bucket_name):
            """Check if GCP bucket exists"""
            url = f"http://{bucket_name}.storage.googleapis.com"
            try:
                response = requests.get(url, timeout=5, verify=False)
                if response.status_code != 404:
                    info = {
                        'name': bucket_name,
                        'url': url,
                        'accessible': response.status_code == 200
                    }
                    cloud_assets['gcp'].append(info)
                    print(f"{Colors.GREEN}[{Colors.CLOUD}] GCP: {bucket_name}{Colors.END}")
            except:
                pass
        
        # Check all patterns
        with ThreadPoolExecutor(max_workers=20) as executor:
            # S3 checks
            s3_futures = [executor.submit(check_s3_bucket, pattern) for pattern in patterns]
            
            # Azure checks
            azure_patterns = [f"{pattern}" for pattern in patterns]
            azure_futures = [executor.submit(check_azure_blob, pattern) for pattern in azure_patterns]
            
            # GCP checks
            gcp_futures = [executor.submit(check_gcp_bucket, pattern) for pattern in patterns]
            
            # Wait for all to complete
            for future in as_completed(s3_futures + azure_futures + gcp_futures):
                pass
        
        self.cloud_assets = cloud_assets
        
        # Summary
        print(f"\n{Colors.GREEN}[{Colors.SUCCESS}] Cloud enumeration complete!{Colors.END}")
        print(f"  S3 Buckets: {len(cloud_assets['s3'])}")
        print(f"  Azure Blobs: {len(cloud_assets['azure'])}")
        print(f"  GCP Buckets: {len(cloud_assets['gcp'])}")
        
        return cloud_assets

    # ==================== UPGRADE 6: MASQUERADE MODE ====================
    def enable_stealth_mode(self, delay=2, rotate_ua=True, use_proxy=False):
        """Enable stealth mode to evade detection"""
        print(f"\n{Colors.YELLOW}[{Colors.EYE}] Enabling stealth mode...{Colors.END}")
        
        self.stealth_mode = True
        self.delay = delay
        
        if rotate_ua:
            print(f"{Colors.CYAN}[{Colors.INFO}] User-Agent rotation enabled ({len(self.user_agents)} UAs){Colors.END}")
        
        if use_proxy:
            # Load some public proxies (in real implementation, you'd want a proxy list)
            self.proxies = ['http://proxy1:8080', 'http://proxy2:8080']
            print(f"{Colors.CYAN}[{Colors.INFO}] Proxy rotation enabled{Colors.END}")
        
        print(f"{Colors.GREEN}[{Colors.SUCCESS}] Stealth mode active (delay: {delay}s){Colors.END}")

    # ==================== UPGRADE 9: DEPENDENCY MAPPER + TECH STACK DETECTOR (MODIFIED) ====================
    def map_dependencies(self, domain, subdomains):
        """Map dependencies between subdomains and detect tech stack - Clean output version"""
        
        dependency_graph = {}
        
        def analyze_subdomain(subdomain):
            deps = set()
            try:
                # Check for subdomain relationships
                parts = subdomain.split('.')
                if len(parts) > 2:  # Has sub-subdomain
                    parent = '.'.join(parts[1:])
                    deps.add(parent)
                
                # Check DNS records for dependencies
                try:
                    # CNAME records often show dependencies
                    answers = self.resolver.resolve(subdomain, 'CNAME')
                    for cname in answers:
                        target = str(cname.target).rstrip('.')
                        deps.add(target)
                except:
                    pass
                
                # Check HTTP for dependencies
                try:
                    url = f"http://{subdomain}"
                    response = requests.get(url, timeout=5, verify=False)
                    
                    # Check for links to other subdomains
                    if response.status_code == 200:
                        # Find links to other subdomains
                        links = re.findall(r'https?://([a-zA-Z0-9.-]+)', response.text)
                        for link in links:
                            if self.domain in link and link != subdomain:
                                deps.add(link)
                except:
                    pass
                
            except Exception as e:
                pass
            
            return subdomain, list(deps)
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(analyze_subdomain, sub): sub for sub in subdomains}
            for future in as_completed(futures):
                sub, deps = future.result()
                if deps:
                    dependency_graph[sub] = deps
        
        self.dependency_graph = dependency_graph
        
        # Print dependency graph (only the results, no warnings or background messages)
        if dependency_graph:
            for sub, deps in dependency_graph.items():
                print(f"  {Colors.GREEN}{sub}{Colors.END} → {', '.join(deps)}")
        else:
            print(f"{Colors.YELLOW}[{Colors.INFO}] No dependencies found{Colors.END}")
        
        return dependency_graph

    # ==================== ENHANCED HUNT FUNCTION ====================
    def hunt(self, domain, quiet=False):
        """Enhanced hunting function with all sources"""
        if not quiet:
            print(f"\n{Colors.PURPLE}[{Colors.GHOST}] Phantom hunting: {Colors.GREEN}{domain}{Colors.END}")
            print(f"{Colors.DIM}{'─'*60}{Colors.END}\n")
        
        self.domain = domain
        all_subdomains = set()
        
        # Sources list
        sources = [
            (self.query_crt_sh, "crt.sh"),
            (self.query_virustotal, "VirusTotal"),
            (self.query_threatcrowd, "ThreatCrowd"),
            (self.query_hackertarget, "HackerTarget"),
            (self.query_rapiddns, "RapidDNS"),
            (self.query_alienvault, "AlienVault"),
            (self.query_urlscan, "URLScan.io"),
            (self.query_securitytrails, "SecurityTrails"),
            (self.query_censys, "Censys")
        ]
        
        def query_source(source_func, source_name):
            try:
                if not quiet:
                    print(f"{Colors.CYAN}[*] Querying {source_name}...{Colors.END}", end='', flush=True)
                
                subs = source_func(domain)
                
                if not quiet:
                    print(f"\r{Colors.GREEN}[{Colors.SUCCESS}] {source_name}: {len(subs)} found{Colors.END}")
                
                return subs
            except Exception as e:
                if not quiet:
                    print(f"\r{Colors.YELLOW}[{Colors.WARNING}] {source_name}: Error - {str(e)[:30]}{Colors.END}")
                return set()
        
        # Query all sources in parallel
        with ThreadPoolExecutor(max_workers=len(sources)) as executor:
            futures = {executor.submit(query_source, func, name): name for func, name in sources}
            for future in as_completed(futures):
                subs = future.result()
                all_subdomains.update(subs)
        
        # Add to main set
        self.subdomains.update(all_subdomains)
        
        if not quiet:
            print(f"\n{Colors.GREEN}[{Colors.SUCCESS}] Hunt complete! Found {len(all_subdomains)} unique subdomains{Colors.END}")
            
            # Display results
            if all_subdomains:
                print(f"\n{Colors.CYAN}Found subdomains:{Colors.END}")
                for sub in sorted(all_subdomains)[:20]:
                    print(f"  {Colors.GREEN}● {sub}{Colors.END}")
                if len(all_subdomains) > 20:
                    print(f"  {Colors.DIM}... and {len(all_subdomains)-20} more{Colors.END}")
        
        return all_subdomains

    # Additional source queries
    def query_securitytrails(self, domain):
        """Query SecurityTrails (free tier)"""
        subdomains = set()
        try:
            url = f"https://securitytrails.com/domain/{domain}/subdomains"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                # Parse subdomains from response
                pattern = r'<a href="/domain/([^"]+)"'
                matches = re.findall(pattern, response.text)
                for match in matches:
                    if match.endswith(domain):
                        subdomains.add(match.lower().strip())
        except:
            pass
        return subdomains

    def query_censys(self, domain):
        """Query Censys (free tier)"""
        subdomains = set()
        try:
            url = f"https://search.censys.io/search?q={domain}&resource=hosts"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                # Parse subdomains from response
                pattern = r'([a-zA-Z0-9.-]+\.' + re.escape(domain) + r')'
                matches = re.findall(pattern, response.text)
                for match in matches:
                    subdomains.add(match.lower().strip())
        except:
            pass
        return subdomains

    # ==================== ENHANCED EXPORT FUNCTION ====================
    def enhanced_export(self, filename):
        """Export results in multiple formats"""
        if not self.subdomains and not self.live_subdomains:
            print(f"{Colors.RED}[{Colors.ERROR}] No results to export{Colors.END}")
            return
        
        try:
            # Prepare export data
            export_data = {
                'target': self.domain,
                'scan_time': datetime.now().isoformat(),
                'statistics': {
                    'total_subdomains': len(self.subdomains),
                    'live_hosts': len(self.live_subdomains),
                    'open_ports': sum(len(ports) for ports in self.ports_open.values()),
                    'cloud_assets': sum(len(assets) for assets in self.cloud_assets.values())
                },
                'subdomains': sorted(list(self.subdomains)),
                'live_hosts': self.live_subdomains,
                'ports': self.ports_open,
                'tech_stack': self.tech_stack,
                'cloud_assets': self.cloud_assets,
                'dependencies': self.dependency_graph
            }
            
            # Determine export format
            if filename.endswith('.json'):
                with open(filename, 'w') as f:
                    json.dump(export_data, f, indent=2)
                print(f"{Colors.GREEN}[{Colors.SUCCESS}] Results exported to {filename} (JSON){Colors.END}")
            
            elif filename.endswith('.html'):
                self.export_html(filename, export_data)
                print(f"{Colors.GREEN}[{Colors.SUCCESS}] Results exported to {filename} (HTML){Colors.END}")
            
            else:  # Default to TXT
                with open(filename, 'w') as f:
                    f.write(f"Phantom Subfinder Results - {self.domain}\n")
                    f.write(f"Scan Time: {datetime.now().isoformat()}\n")
                    f.write("="*50 + "\n\n")
                    
                    f.write(f"Total Subdomains: {len(self.subdomains)}\n")
                    f.write(f"Live Hosts: {len(self.live_subdomains)}\n\n")
                    
                    f.write("SUBDOMAINS:\n")
                    for sub in sorted(self.subdomains):
                        f.write(f"  {sub}\n")
                    
                    if self.live_subdomains:
                        f.write("\nLIVE HOSTS:\n")
                        for host, info in self.live_subdomains.items():
                            f.write(f"  {host} - {info}\n")
                
                print(f"{Colors.GREEN}[{Colors.SUCCESS}] Results exported to {filename} (TXT){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[{Colors.ERROR}] Export failed: {e}{Colors.END}")

    def export_html(self, filename, data):
        """Export results as HTML report"""
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Phantom Subfinder Report - {data['target']}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background: #0a0e27; color: #fff; }}
                h1, h2, h3 {{ color: #00ff9d; }}
                .container {{ max-width: 1200px; margin: auto; }}
                .stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 20px 0; }}
                .stat-card {{ background: #1a1f3a; padding: 20px; border-radius: 10px; border-left: 4px solid #00ff9d; }}
                .stat-value {{ font-size: 24px; font-weight: bold; color: #00ff9d; }}
                .stat-label {{ color: #888; }}
                .subdomain {{ background: #1a1f3a; padding: 10px; margin: 5px 0; border-radius: 5px; }}
                .live {{ border-left: 4px solid #00ff9d; }}
                .port {{ display: inline-block; background: #2a2f4a; padding: 5px 10px; margin: 2px; border-radius: 3px; }}
                .tech-tag {{ display: inline-block; background: #3a3f5a; padding: 3px 8px; margin: 2px; border-radius: 3px; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>👻 Phantom Subfinder Report</h1>
                <p>Target: <strong>{data['target']}</strong> | Scan Time: {data['scan_time']}</p>
                
                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-value">{data['statistics']['total_subdomains']}</div>
                        <div class="stat-label">Total Subdomains</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{data['statistics']['live_hosts']}</div>
                        <div class="stat-label">Live Hosts</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{data['statistics']['open_ports']}</div>
                        <div class="stat-label">Open Ports</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{data['statistics']['cloud_assets']}</div>
                        <div class="stat-label">Cloud Assets</div>
                    </div>
                </div>
                
                <h2>Live Hosts</h2>
                {self.generate_html_live_hosts(data['live_hosts'])}
                
                <h2>Technology Stack</h2>
                {self.generate_html_tech_stack(data['tech_stack'])}
                
                <h2>Cloud Assets</h2>
                {self.generate_html_cloud(data['cloud_assets'])}
            </div>
        </body>
        </html>
        """
        
        with open(filename, 'w') as f:
            f.write(html_template)

    def generate_html_live_hosts(self, live_hosts):
        """Generate HTML for live hosts"""
        html = ""
        for host, info in live_hosts.items():
            status_color = "green" if info.get('status_code', 0) < 400 else "orange" if info.get('status_code', 0) < 500 else "red"
            html += f"""
            <div class="subdomain live">
                <strong>{host}</strong>
                <span style="color: {status_color};">[{info.get('status_code', 'N/A')}]</span>
                <div style="margin-top: 5px;">
                    <span class="tech-tag">Title: {info.get('title', 'N/A')}</span>
                    <span class="tech-tag">Server: {info.get('server', 'Unknown')}</span>
                </div>
            </div>
            """
        return html

    def generate_html_tech_stack(self, tech_stack):
        """Generate HTML for technology stack"""
        html = ""
        for host, techs in tech_stack.items():
            html += f"<div><strong>{host}</strong>: "
            for tech in techs:
                html += f'<span class="tech-tag">{tech}</span> '
            html += "</div>"
        return html

    def generate_html_cloud(self, cloud_assets):
        """Generate HTML for cloud assets"""
        html = ""
        for provider, assets in cloud_assets.items():
            if assets:
                html += f"<h3>{provider.upper()}</h3>"
                for asset in assets:
                    html += f'<div class="subdomain">{asset["url"]}</div>'
        return html

    # ==================== FULL RECON COMMAND ====================
    def full_recon(self, domain, output=None):
        """Run complete reconnaissance suite"""
        print(f"\n{Colors.PURPLE}{'='*70}{Colors.END}")
        print(f"{Colors.YELLOW}[{Colors.CROWN}] PHANTOM FULL RECONNAISSANCE MODE{Colors.END}")
        print(f"{Colors.PURPLE}{'='*70}{Colors.END}\n")
        
        start_time = time.time()
        
        # Phase 1: Subdomain Enumeration
        print(f"{Colors.CYAN}[Phase 1] Subdomain Enumeration{Colors.END}")
        self.hunt(domain)
        
        # Phase 2: Brute Force
        print(f"\n{Colors.CYAN}[Phase 2] Brute Force Enhancement{Colors.END}")
        brute_subs = self.enhanced_bruteforce(domain, threads=100, wordlist='heavy')
        self.subdomains.update(brute_subs)
        
        # Phase 3: Live Host Validation
        print(f"\n{Colors.CYAN}[Phase 3] Live Host Validation{Colors.END}")
        live_hosts = self.live_host_validation(self.subdomains)
        
        # Phase 4: Port Scanning
        if live_hosts:
            print(f"\n{Colors.CYAN}[Phase 4] Port Scanning{Colors.END}")
            self.enhanced_port_scan(live_hosts.keys(), top_ports=100)
        
        # Phase 5: Cloud Enumeration
        print(f"\n{Colors.CYAN}[Phase 5] Cloud Asset Discovery{Colors.END}")
        self.enumerate_cloud_assets(domain)
        
        # Phase 6: Tech Stack Detection
        print(f"\n{Colors.CYAN}[Phase 6] Technology Fingerprinting{Colors.END}")
        self.map_dependencies(domain, live_hosts.keys())
        
        elapsed = time.time() - start_time
        
        # Final Summary
        print(f"\n{Colors.PURPLE}{'='*70}{Colors.END}")
        print(f"{Colors.GREEN}[{Colors.SUCCESS}] FULL RECON COMPLETE!{Colors.END}")
        print(f"{Colors.PURPLE}{'='*70}{Colors.END}")
        print(f"{Colors.CYAN}Time elapsed: {elapsed:.2f} seconds{Colors.END}")
        print(f"{Colors.CYAN}Total subdomains: {len(self.subdomains)}{Colors.END}")
        print(f"{Colors.CYAN}Live hosts: {len(self.live_subdomains)}{Colors.END}")
        print(f"{Colors.CYAN}Open ports discovered: {sum(len(ports) for ports in self.ports_open.values())}{Colors.END}")
        print(f"{Colors.CYAN}Cloud assets: {sum(len(assets) for assets in self.cloud_assets.values())}{Colors.END}")
        
        # Export if output specified
        if output:
            self.enhanced_export(output)

    # ==================== MAIN RUN LOOP ====================
    def run(self):
        """Enhanced main interactive loop"""
        self.banner()
        print(f"{Colors.GREEN}Type '{Colors.YELLOW}help{Colors.GREEN}' for available commands (V2.0 features available!){Colors.END}")
        
        while True:
            try:
                cmd_line = input(f"\n{Colors.PURPLE}phantom@{Colors.CYAN}subfinder{Colors.BLUE} → {Colors.END}").strip()
                
                if not cmd_line:
                    continue
                
                # Parse command and arguments
                parts = cmd_line.split()
                cmd = parts[0].lower()
                
                if cmd == 'exit' or cmd == 'quit':
                    print(f"{Colors.PURPLE}[{Colors.GHOST}] Phantom returns to the shadows...{Colors.END}")
                    break
                
                elif cmd == 'help':
                    self.print_enhanced_help()
                
                elif cmd == 'clear':
                    self.banner()
                
                # ========== HUNT COMMAND ==========
                elif cmd == 'hunt' and len(parts) >= 2:
                    domain = parts[1]
                    if self.check_domain(domain):
                        self.hunt(domain)
                    else:
                        print(f"{Colors.RED}[{Colors.ERROR}] Invalid domain format{Colors.END}")
                
                # ========== BRUTEFORCE COMMAND (Enhanced) ==========
                elif cmd == 'bruteforce' and len(parts) >= 2:
                    domain = parts[1]
                    threads = 50
                    wordlist = 'common'
                    
                    # Parse arguments
                    for i in range(2, len(parts)):
                        if parts[i] == '--threads' and i+1 < len(parts):
                            threads = int(parts[i+1])
                        elif parts[i] == '--wordlist' and i+1 < len(parts):
                            wordlist = parts[i+1]
                    
                    if self.check_domain(domain):
                        self.domain = domain
                        subs = self.enhanced_bruteforce(domain, threads, wordlist)
                        self.subdomains.update(subs)
                    else:
                        print(f"{Colors.RED}[{Colors.ERROR}] Invalid domain{Colors.END}")
                
                # ========== SCAN COMMAND (Enhanced) ==========
                elif cmd == 'scan' and len(parts) >= 2:
                    domain = parts[1]
                    live_check = '--live' in parts
                    ports = None
                    
                    # Parse port arguments
                    if '--ports' in parts:
                        idx = parts.index('--ports')
                        if idx + 1 < len(parts):
                            port_arg = parts[idx + 1]
                            if ',' in port_arg:
                                ports = [int(p) for p in port_arg.split(',')]
                            elif '-' in port_arg:
                                start, end = map(int, port_arg.split('-'))
                                ports = list(range(start, end + 1))
                            else:
                                ports = [int(port_arg)]
                    elif '--top-ports' in parts:
                        idx = parts.index('--top-ports')
                        if idx + 1 < len(parts):
                            top = int(parts[idx + 1])
                            ports = None  # Will use default top ports
                    
                    if not self.subdomains:
                        print(f"{Colors.YELLOW}[{Colors.INFO}] No subdomains found. Hunting first...{Colors.END}")
                        self.hunt(domain)
                    
                    if self.subdomains:
                        if live_check:
                            live = self.live_host_validation(self.subdomains)
                            if live:
                                self.enhanced_port_scan(live.keys(), ports)
                        else:
                            # Just resolve
                            resolved = self.resolve_subdomains(self.subdomains)
                            if resolved and ports:
                                self.enhanced_port_scan(resolved, ports)
                    else:
                        print(f"{Colors.RED}[{Colors.ERROR}] No subdomains to scan{Colors.END}")
                
                # ========== RECURSE COMMAND (New) ==========
                elif cmd == 'recurse' and len(parts) >= 2:
                    domain = parts[1]
                    depth = 2
                    
                    if '--depth' in parts:
                        idx = parts.index('--depth')
                        if idx + 1 < len(parts):
                            depth = int(parts[idx + 1])
                    
                    if self.check_domain(domain):
                        subs = self.recursive_hunt(domain, depth)
                        self.subdomains.update(subs)
                        print(f"\n{Colors.GREEN}[{Colors.SUCCESS}] Recursive hunt complete! Found {len(subs)} subdomains{Colors.END}")
                    else:
                        print(f"{Colors.RED}[{Colors.ERROR}] Invalid domain{Colors.END}")
                
                # ========== CLOUD COMMAND (New) ==========
                elif cmd == 'cloud' and len(parts) >= 2:
                    domain = parts[1]
                    if self.check_domain(domain):
                        self.enumerate_cloud_assets(domain)
                    else:
                        print(f"{Colors.RED}[{Colors.ERROR}] Invalid domain{Colors.END}")
                
                # ========== MAP COMMAND (New - MODIFIED FOR CLEAN OUTPUT) ==========
                elif cmd == 'map' and len(parts) >= 2:
                    domain = parts[1]
                    if self.subdomains:
                        self.map_dependencies(domain, self.subdomains)
                    else:
                        print(f"{Colors.YELLOW}[{Colors.INFO}] No subdomains found. Hunting first...{Colors.END}")
                        self.hunt(domain)
                        if self.subdomains:
                            self.map_dependencies(domain, self.subdomains)
                
                # ========== STEALTH COMMAND (New) ==========
                elif cmd == 'stealth' and len(parts) >= 2:
                    domain = parts[1]
                    delay = 2
                    
                    if '--delay' in parts:
                        idx = parts.index('--delay')
                        if idx + 1 < len(parts):
                            delay = int(parts[idx + 1])
                    
                    self.enable_stealth_mode(delay=delay, rotate_ua=True)
                    print(f"{Colors.YELLOW}[{Colors.INFO}] Running stealth hunt...{Colors.END}")
                    self.hunt(domain)
                
                # ========== FULL-RECON COMMAND (New) ==========
                elif cmd == 'full-recon' and len(parts) >= 2:
                    domain = parts[1]
                    output = None
                    
                    if '--output' in parts:
                        idx = parts.index('--output')
                        if idx + 1 < len(parts):
                            output = parts[idx + 1]
                    
                    self.full_recon(domain, output)
                
                # ========== EXPORT COMMAND (Enhanced) ==========
                elif cmd == 'export' and len(parts) >= 2:
                    filename = parts[1]
                    self.enhanced_export(filename)
                
                else:
                    print(f"{Colors.RED}[{Colors.ERROR}] Unknown command. Type 'help' for available commands{Colors.END}")
            
            except KeyboardInterrupt:
                print(f"\n{Colors.PURPLE}[{Colors.GHOST}] Phantom vanishes abruptly...{Colors.END}")
                break
            except Exception as e:
                print(f"{Colors.RED}[{Colors.ERROR}] Error: {e}{Colors.END}")
                import traceback
                traceback.print_exc()

    # ==================== UTILITY FUNCTIONS ====================
    def check_domain(self, domain):
        """Validate domain format"""
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9]'  # First character
            r'(?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)'  # Sub domain
            r'+[a-zA-Z]{2,}$'  # TLD
        )
        return bool(domain_regex.match(domain))

    def resolve_subdomains(self, subdomains):
        """Resolve subdomains to verify they're alive"""
        live = set()
        
        print(f"\n{Colors.YELLOW}[*] Resolving {len(subdomains)} subdomains...{Colors.END}")
        
        def resolve(sub):
            try:
                answers = self.resolver.resolve(sub, 'A')
                if answers:
                    live.add(sub)
                    ips = [str(rdata) for rdata in answers]
                    print(f"{Colors.GREEN}[{Colors.SUCCESS}] Alive: {sub} -> {', '.join(ips)}{Colors.END}")
            except:
                print(f"{Colors.RED}[{Colors.ERROR}] Dead: {sub}{Colors.END}")
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            list(executor.map(resolve, subdomains))
        
        return live

    # Original source query methods (kept from original)
    def query_crt_sh(self, domain):
        """Query crt.sh for SSL certificate subdomains"""
        subdomains = set()
        try:
            url = f"https://crt.sh/?q=%25.{domain}&output=json"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                data = response.json()
                for entry in data:
                    name = entry.get('name_value', '')
                    if name:
                        for sub in name.split('\n'):
                            if sub.endswith(domain) and '*' not in sub:
                                subdomains.add(sub.lower().strip())
        except Exception as e:
            pass
        return subdomains

    def query_virustotal(self, domain):
        """Query VirusTotal"""
        subdomains = set()
        try:
            url = f"https://www.virustotal.com/ui/domains/{domain}/subdomains"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                data = response.json()
                for item in data.get('data', []):
                    sub = item.get('id', '')
                    if sub.endswith(domain):
                        subdomains.add(sub.lower().strip())
        except Exception:
            pass
        return subdomains

    def query_threatcrowd(self, domain):
        """Query ThreatCrowd API"""
        subdomains = set()
        try:
            url = f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                data = response.json()
                for sub in data.get('subdomains', []):
                    if sub.endswith(domain):
                        subdomains.add(sub.lower().strip())
        except Exception:
            pass
        return subdomains

    def query_hackertarget(self, domain):
        """Query HackerTarget"""
        subdomains = set()
        try:
            url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                for line in response.text.split('\n'):
                    if ',' in line:
                        sub = line.split(',')[0].strip()
                        if sub.endswith(domain):
                            subdomains.add(sub.lower())
        except Exception:
            pass
        return subdomains

    def query_rapiddns(self, domain):
        """Query RapidDNS"""
        subdomains = set()
        try:
            url = f"https://rapiddns.io/subdomain/{domain}"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                pattern = r'target="_blank">([a-zA-Z0-9.-]+\.' + re.escape(domain) + r')</a>'
                found = re.findall(pattern, response.text)
                for sub in found:
                    subdomains.add(sub.lower().strip())
        except Exception:
            pass
        return subdomains

    def query_alienvault(self, domain):
        """Query AlienVault OTX"""
        subdomains = set()
        try:
            url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                data = response.json()
                for entry in data.get('passive_dns', []):
                    sub = entry.get('hostname', '')
                    if sub.endswith(domain):
                        subdomains.add(sub.lower().strip())
        except Exception:
            pass
        return subdomains

    def query_urlscan(self, domain):
        """Query URLScan.io"""
        subdomains = set()
        try:
            url = f"https://urlscan.io/api/v1/search/?q=domain:{domain}"
            headers = {'User-Agent': self.get_random_user_agent()}
            response = requests.get(url, headers=headers, timeout=self.timeout, verify=False)
            if response.status_code == 200:
                data = response.json()
                for result in data.get('results', []):
                    page = result.get('page', {})
                    sub = page.get('domain', '')
                    if sub.endswith(domain):
                        subdomains.add(sub.lower().strip())
        except Exception:
            pass
        return subdomains

def main():
    """Main entry point"""
    # Parse command line arguments for direct mode
    parser = argparse.ArgumentParser(description='Phantom Subfinder v2.0 - Ultimate Recon Tool')
    parser.add_argument('-d', '--domain', help='Target domain')
    parser.add_argument('-m', '--mode', choices=['hunt', 'bruteforce', 'full'], default='hunt', help='Scan mode')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('--threads', type=int, default=50, help='Number of threads')
    parser.add_argument('--wordlist', choices=['common', 'heavy'], default='common', help='Wordlist to use')
    
    args = parser.parse_args()
    
    # Auto-setup runs first
    phantom_auto_setup()
    
    # Create enhanced phantom
    phantom = EnhancedPhantomSubfinder()
    
    # If domain provided via command line, run directly
    if args.domain:
        if args.mode == 'hunt':
            phantom.hunt(args.domain)
        elif args.mode == 'bruteforce':
            phantom.enhanced_bruteforce(args.domain, args.threads, args.wordlist)
        elif args.mode == 'full':
            phantom.full_recon(args.domain, args.output)
        
        if args.output:
            phantom.enhanced_export(args.output)
    else:
        # Interactive mode
        phantom.run()

if __name__ == "__main__":
    main()