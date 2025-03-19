# httpdump
Docker image to log get/post requests to console for debugging/analysis.

## setup
The port can be changed via either of these options:
```bash
docker run -e PORT=8080 -p 8080:8080 blackheart-tf/httpdump
```
This option is shorter to type, but your port message wont be correct, not to keep ":80":
```bash
docker run -p 8080:80 blackheart-tf/httpdump
```