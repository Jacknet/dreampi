# dreampi
An environment-agnostic fork of [DreamPi](https://github.com/Kazade/dreampi) which can run on most GNU/Linux flavors that can run Python 2.7, optimized for use with devices outside of a Dreamcast.

## Prerequisites
Install the following dependencies through PIP:
1. pyserial
1. sh
1. python-iptables
1. miniupnpc

Make sure to set a `XTABLES_LIBDIR` environment variable to the location containing your xtables libraries (e.g. `/usr/lib64/xtables/`).

This program will use `dnsmasq` as the DNS daemon. More modern variants of GNU/Linux use `systemd-resolved`, which may end up reserving certain service ports. Please make sure to set `dnsmasq` for DNS service when possible.

Copy the `dnsmasq.conf` file in the `etc` directory of this repo to your target system's `/etc/` directory. Make sure to back up any existing `dnsmasq.conf` in there or rename it by appending a `.bak` to the file name.

## Usage
As root, operate the DreamPi service using the following command:<br>
`sudo python2 dreampi.py [start|stop|restart] interface`

The `interface` parameter corresponds to your network device, such as `eth0` or `wlan0`. Check `ifconfig` to know your network device's name.

You do not need to define your network interface if you are stopping the service.

---

Original by @Kazade

A daemon that creates a bridge between a Dreamcast's Dial-up Modem, and the Internet via the Pi
