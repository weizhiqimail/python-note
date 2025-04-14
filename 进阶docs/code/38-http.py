# -*- encoding: utf-8 -*-

from wsgiref.simple_server import make_server


def render(path):
    with open(path, 'rb') as f:
        return f.read()


def index(environ):
    return render('html/index.html')


def login(req):
    print('req: ', req)
    method = req['REQUEST_METHOD'].upper()
    print('--------------------------------------------------------')
    print('method: ', method)
    if method == 'GET':
        return render('html/login.html')
    elif method == 'POST':
        username = req['QUERY_STRING']
        print('username')
        print(username)
        return render('html/login-post.html')


def signup():
    pass


def router():
    urlpatterns = [
        ('/', index),
        ('/login/', login),
        ('/signup/', signup),
    ]
    return urlpatterns


def application(environ, start_response):
    path_info = environ['PATH_INFO']
    print(path_info)

    if path_info[-1] != '/':
        path_info += '/'
    start_response('200 OK', [('Content-Type', 'text/html')])

    urlpatterns = router()

    func = None

    for item in urlpatterns:
        if item[0] == path_info:
            func = item[1]
            break
    print('func')
    print(func)
    if func is None:
        return [render('html/404.html')]

    return [func(environ)]


PORT = 8080

httpd = make_server('', PORT, application)

print('server is running at http://localhost:{port}'.format(port=PORT))

httpd.serve_forever()

d = {
    'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\weizh\\AppData\\Roaming',
    'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
    'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
    'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'CARL',
    'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'CONDA_DEFAULT_ENV': 'base',
    'CONDA_PREFIX': 'D:\\software\\anaconda\\install', 'CONDA_PROMPT_MODIFIER': '(base) ', 'CONDA_SHLVL': '1',
    'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'ERLANG_HOME': 'D:\\software\\erlang\\erl10.4',
    'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
    'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\weizh',
    'IDEA_INITIAL_DIRECTORY': 'D:\\software\\pycharm\\PyCharm 2019.2.1\\bin',
    'LOCALAPPDATA': 'C:\\Users\\weizh\\AppData\\Local', 'LOGONSERVER': '\\\\CARL',
    'MOZ_PLUGIN_PATH': 'D:\\software\\foxitReader\\Foxit Reader\\plugins\\', 'NUMBER_OF_PROCESSORS': '8',
    'ONEDRIVECONSUMER': 'C:\\Users\\weizh\\OneDrive', 'OS': 'Windows_NT',
    'PATH': 'D:\\software\\anaconda\\install;D:\\software\\anaconda\\install\\Library\\mingw-w64\\bin;D:\\software\\anaconda\\install\\Library\\usr\\bin;D:\\software\\anaconda\\install\\Library\\bin;D:\\software\\anaconda\\install\\Scripts;D:\\software\\anaconda\\install\\bin;D:\\software\\anaconda\\install;D:\\software\\anaconda\\install\\Library\\mingw-w64\\bin;D:\\software\\anaconda\\install\\Library\\usr\\bin;D:\\software\\anaconda\\install\\Library\\bin;D:\\software\\anaconda\\install\\Scripts;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0;C:\\Windows\\System32\\OpenSSH;C:\\Program Files\\Intel\\WiFi\\bin;C:\\Program Files\\Common Files\\Intel\\WirelessCommon;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;D:\\software\\git\\Git\\cmd;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;D:\\software\\node;D:\\software\\MongoDB\\bin;D:\\software\\tortoiseGit\\bin;D:\\software\\node\\npm_packages_cache;D:\\software\\redis;C:\\Program Files\\dotnet;C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python37_64;D:\\software\\anaconda\\install\\condabin;D:\\software\\webstorm\\WebStorm 2019.2.1\\bin;D:\\software\\pycharm\\PyCharm 2019.2.1\\bin;C:\\Program Files\\MySQL\\MySQL Shell 8.0\\bin;C:\\Users\\weizh\\AppData\\Local\\atom\\bin',
    'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64',
    'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 142 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6',
    'PROCESSOR_REVISION': '8e0a', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files',
    'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(base) $P$G',
    'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
    'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'D:\\software\\pycharm\\PyCharm 2019.2.1\\bin;',
    'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8',
    'PYTHONPATH': 'F:\\program\\python\\python-note;D:\\software\\pycharm\\PyCharm 2019.2.1\\helpers\\pycharm_matplotlib_backend;D:\\software\\pycharm\\PyCharm 2019.2.1\\helpers\\pycharm_display',
    'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows',
    'TEMP': 'C:\\Users\\weizh\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\weizh\\AppData\\Local\\Temp',
    'USERDOMAIN': 'CARL', 'USERDOMAIN_ROAMINGPROFILE': 'CARL', 'USERNAME': 'weizh',
    'USERPROFILE': 'C:\\Users\\weizh', 'WEBSTORM': 'D:\\software\\webstorm\\WebStorm 2019.2.1\\bin;',
    'WINDIR': 'C:\\Windows', 'SERVER_NAME': 'carl', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8080',
    'REMOTE_HOST': '', 'CONTENT_LENGTH': '0', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1',
    'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'POST', 'PATH_INFO': '/login', 'QUERY_STRING': '',
    'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'application/x-www-form-urlencoded',
    'HTTP_HOST': 'localhost:8080', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_CACHE_CONTROL': 'max-age=0',
    'HTTP_ORIGIN': 'http://localhost:8080', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'HTTP_SEC_FETCH_SITE': 'same-origin', 'HTTP_REFERER': 'http://localhost:8080/login',
    'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'HTTP_COOKIE': 'username-localhost-8888="2|1:0|10:1570263553|23:username-localhost-8888|44:NjBkMjZjMDI1MWM1NDhhNzg2MDM0YTgyODUxY2YzYTc=|29fc08e33361e929b5a50f714e3e9e5b5545ad18faede830fbfe72dc2e8bc3f2"; _xsrf=2|cdb1b5da|816558598ba33db57c1ca924afde233d|1570263553',
}
