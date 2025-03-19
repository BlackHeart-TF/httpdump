# httpdump
Docker image to log get/post requests to console for debugging/analysis.

## setup
Fist build the image from git
```bash
docker build -t httpdump https://github.com/BlackHeart-TF/httpdump.git\#main
```
then run with
```bash
docker run httpdump
```

### configuration
The port can be changed via either of these options:
```bash
docker run -e PORT=8080 -p 8080:8080 httpdump
```
This option is shorter to type, but your port message wont be correct, note to keep ":80":
```bash
docker run -p 8080:80 httpdump
```