# builder
builder yaml


## Usage

```
$ python3 ./example.py --help
usage: example.py [-h] [-i IP] [-o OS] [-c CPU] [-m MEM]

optional arguments:
  -h, --help         show this help message and exit
  -i IP, --ip IP     127.0.0.0/8
  -o OS, --os OS     RHEL8.3
  -c CPU, --cpu CPU  2
  -m MEM, --mem MEM  8
```

## Example

```
$ python3 ./example.py -c 2 -m 4 -o Windows2019 
Running builder...
!!python/object:builder.Builder
cidr: 8
cpu: '2'
gateway: 127.0.0.1
ip: 127.0.0.0
mem: '4'
netmask: 255.0.0.0
network: 127.0.0.0
os: Windows2019
```

## Author

&ldquo;Joel E Carlson&rdquo; &lt;joel.elmer.carlson@gmail.com&gt;
