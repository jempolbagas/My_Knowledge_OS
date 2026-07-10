---
title: "(CN-9a) IPv6 Lecture Notes"
course: ""
tags: []
aliases: ["(CN-9a) IPv6 Lecture Notes"]
created: "2026-06-24"
---
# Comprehensive Guide to IPv6: Addressing, Configuration, and Transition

## 1. Introduction: The Need for IPv6
The necessity for IPv6 primarily stems from the depletion of IPv4 addresses. IPv6 acts as the successor to IPv4, offering a vastly larger 128-bit address space compared to IPv4's 32-bit limitation. The development of IPv6 goes beyond just increasing address space; it also includes improvements to resolve IPv4's limitations and addresses issues related to Network Address Translation (NAT) and the rapid growth of the Internet of Things (IoT).

### Transition Techniques
IPv4 and IPv6 will coexist for several years. The IETF has developed protocols to help network administrators migrate using three main techniques:
*   **Dual Stack:** Devices run both IPv4 and IPv6 protocols simultaneously.
*   **Tunneling:** A method to transport IPv6 packets across an IPv4 network by encapsulating the IPv6 packet inside an IPv4 packet.
*   **Translation (NAT64):** Allows IPv6-enabled devices to communicate with IPv4-enabled devices using translation techniques similar to IPv4 NAT.
*   *Note:* Tunneling and translation are intended as transitional mechanisms toward native IPv6 communication and should only be used when necessary.

## 2. Foundational Concepts: Number Systems
To understand IPv6, it is crucial to understand Hexadecimal and Binary conversions.
*   Hexadecimal uses 16 digits: 0-9 and A-F (representing 10-15).
*   One hexadecimal digit represents exactly 4 bits (a nibble).
*   Converting Hex to Binary involves separating each hex digit into its corresponding 4-bit binary sequence.

## 3. IPv6 Address Formatting and Rules
IPv6 addresses are 128 bits long and written in hexadecimal format. They are not case-sensitive.
*   **Format:** The standard format is `X:X:X:X:X:X:X:X`, where each 'X' is a "hextet" consisting of 4 hexadecimal values (16 bits). There are 8 hextets in total.

### Compression Rules
To simplify the writing of IPv6 addresses, two primary rules are applied:
1.  **Omitting Leading Zeros:** Leading zeros in any 16-bit hextet can be removed. For example, `01ab` becomes `1ab`, and `009f0` becomes `9f0`. *Note:* This rule does not apply to trailing zeros.
2.  **Double Colon (::):** A double colon can replace a single contiguous string of one or more 16-bit hextets that consist entirely of zeros. *Crucial Note:* The double colon `::` can only be used once per IPv6 address to avoid ambiguity.

## 4. Types of IPv6 Communication
IPv6 categories network traffic into three general types:
*   **Unicast:** Uniquely identifies a single interface on an IPv6-enabled device.
*   **Multicast:** Used to send a single IPv6 packet to multiple destinations simultaneously.
*   **Anycast:** An IPv6 unicast address assigned to multiple devices. A packet sent to an anycast address is routed to the nearest device holding that address.
*   *Note on Broadcast:* Unlike IPv4, IPv6 does not have a broadcast address. Instead, it uses an "all-nodes multicast address" to achieve similar results.

## 5. Unicast Addresses: GUA and LLA
An IPv6 device can have multiple IPv6 addresses. Prefix lengths, represented in slash notation (e.g., `/64`), indicate the network portion of the address. A `/64` prefix is highly recommended for most networks because it simplifies subnetting and accommodates Stateless Address Autoconfiguration (SLAAC) which requires a 64-bit Interface ID.

### Global Unicast Address (GUA)
*   GUAs are globally unique and routable across the IPv6 internet, similar to public IPv4 addresses.
*   Currently, distributed GUAs start with a `001` binary sequence (the `2000::/3` prefix), which covers the range from `2000` to `3fff`.
*   **Structure:** A standard `/64` GUA consists of a 48-bit Global Routing Prefix (assigned by an ISP), a 16-bit Subnet ID (managed internally by an organization), and a 64-bit Interface ID (the host portion).

### Link-Local Address (LLA)
*   LLAs are mandatory for every IPv6-enabled network interface.
*   They are used strictly for local-link communication (within the same subnet) and cannot be routed.
*   Hosts use the local router's LLA as their default gateway. Routers use neighbor LLAs for routing updates.
*   **Structure:** LLAs reside within the `fe80::/10` range. The first 10 bits are `1111 1110 10`, making the first hextet range between `fe80` and `febf`.

## 6. Static and Dynamic Configuration

### Static Configuration
*   **Router GUA:** Configured via the `ipv6 address <ipv6-address>/<prefix-length>` command on an interface.
*   **Router LLA:** Configured using the `ipv6 address <ipv6-link-local-address> link-local` command.
*   **Hosts:** Configured manually similar to IPv4, commonly utilizing the router's LLA as the default gateway.

### Dynamic Configuration (ICMPv6 RS and RA)
Devices dynamically obtain configurations using ICMPv6 Router Solicitation (RS) and Router Advertisement (RA) messages. Hosts send RS messages to find routers, and routers reply with RA messages providing network prefix, default gateway, and DNS info. RAs provide three configuration methods:
1.  **SLAAC (Stateless Address Autoconfiguration):** Devices generate their own GUA without a DHCPv6 server. They use the prefix from the RA message and create a 64-bit Interface ID using the EUI-64 process (derived from the MAC address) or a randomly generated number.
2.  **SLAAC and Stateless DHCPv6:** Devices use SLAAC to create their IP and gateway but contact a stateless DHCPv6 server to get DNS server and domain name information.
3.  **Stateful DHCPv6:** Similar to IPv4 DHCP, the device relies completely on a DHCPv6 server to receive its GUA, DNS, and other information.

### Dynamic LLA Generation
Just like GUAs, LLAs can be dynamically assigned. They combine the `fe80::/10` prefix with an Interface ID generated via EUI-64 or randomly. Cisco routers, by default, utilize EUI-64 to auto-generate the Interface ID for LLAs on IPv6 interfaces once a GUA is assigned.

## 7. IPv6 Multicast Addresses
IPv6 Multicast addresses fall into the `ff00::/8` range (first hextet starts with `1111 1111`). Multicast addresses are only valid as destination addresses.

### Well-Known Multicast
Used for predefined groups of devices:
*   `ff02::1` (All-nodes multicast group): Reaches all IPv6-enabled devices on the local link (effectively replacing IPv4 broadcast).
*   `ff02::2` (All-routers multicast group): Reaches all IPv6 routers on the link.

### Solicited-Node Multicast
*   Similar to all-nodes multicast but more efficient.
*   It maps to a special Ethernet multicast address, allowing an Ethernet NIC to filter frames at the hardware level (by checking the destination MAC address) without interrupting the device's main processor unless the packet is truly intended for it.
