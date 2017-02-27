#!/bin/vbash
source /opt/vyatta/etc/functions/script-template

# work in progress, expect future updates
# todo: make lots of interface-based firewall rules

# ---------------- Variables -------------------
HOSTNAME="loki"

# ============ VyOS Config Script ==============
# -------------- Hannah Pearson ----------------

configure

set system host-name ${HOSTNAME}

# ignore ICMP redirect messages, which update routing info
set firewall receive-redirects disable
set firewall ipv6-receive-redirects disable

# drop packets containing source route info in header
# this may be an indicator of spoofed packets
set firewall ip-src-route disable
set firewall ipv6-src-route disable

# log packets with likely invalid source/destination information
# this also may indicate spoofed packets
set firewall log-martians enable

# if setting up connection tracking:
# this will enable logging of new tcp connections
# set system conntrack log tcp new

commit
