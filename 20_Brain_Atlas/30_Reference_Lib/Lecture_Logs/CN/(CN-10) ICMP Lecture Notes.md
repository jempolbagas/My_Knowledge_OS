---
title: "(CN-10) ICMP Lecture Notes"
course: ""
tags: []
aliases: ["(CN-10) ICMP Lecture Notes"]
created: "2026-06-24"
---
# Comprehensive Guide to Internet Control Message Protocol (ICMP)

**Course:** Jaringan Komputer  
**Instructor:** Herdito Ibnu Dewangkoro (Informatika UNS)  

---

## 1. Introduction to ICMP
The Internet Control Message Protocol (ICMP) is a critical network layer protocol used by devices to provide feedback about issues related to the processing of IP packets under specific conditions. 

* **ICMPv4:** The standard messaging protocol for IPv4 networks.
* **ICMPv6:** The messaging protocol for IPv6 networks, which includes significant additional functionality compared to its predecessor.

**Common ICMP Messages (Both IPv4 and IPv6):**
* Host Reachability
* Destination or Service Unreachable
* Time Exceeded

---

## 2. Core ICMP Messages

### Host Reachability
ICMP Echo Messages are utilized to test the reachability of a host on an IP network. 
* A local host sends an **ICMP Echo Request** to a destination IP address.
* If the destination host is available and operating correctly, it responds with an **Echo Reply**.

### Destination or Service Unreachable
An ICMP Destination Unreachable message notifies the source that a specific destination or service cannot be reached. These messages include specific codes indicating the exact reason the packet could not be delivered.

**Common Destination Unreachable Codes for ICMPv4:**
* `00` - Net unreachable
* `01` - Host unreachable
* `02` - Protocol unreachable
* `03` - Port unreachable

**Common Destination Unreachable Codes for ICMPv6:**
* `00` - No route to destination
* `01` - Communication with the destination is administratively prohibited (e.g., blocked by a firewall)
* `02` - Beyond the scope of the source address
* `03` - Address unreachable
* `04` - Port unreachable

### Time Exceeded
When a packet traverses a network, its lifespan is limited to prevent infinite routing loops.
* **IPv4:** When the Time to Live (TTL) field in a packet is decremented to `0`, an ICMPv4 Time Exceeded message is sent back to the source host.
* **IPv6:** ICMPv6 functions similarly but uses the IPv6 **Hop Limit** field instead of the TTL field to determine if a packet has expired.
* *Note:* The Time Exceeded message is the core mechanism used by network diagnostic tools like `traceroute`.

---

## 3. ICMPv6 Specific Messages (Neighbor Discovery Protocol)

ICMPv6 introduces new features and enhanced functionality not found in ICMPv4. This includes four new protocols that make up the **Neighbor Discovery Protocol (NDP)**.

### Router Messaging (Dynamic Address Allocation)
Communication between IPv6 routers and IPv6 devices handles dynamic address allocation using:
1. **Router Solicitation (RS) message:** Sent by an IPv6 host (e.g., upon booting up) to discover if there is an IPv6 router on the network and to request dynamic IPv6 configuration information.
2. **Router Advertisement (RA) message:** Sent by an IPv6 router every 200 seconds, or in response to an RS message. It provides addressing information to hosts, such as the network prefix, prefix length, DNS address, and domain name. Hosts using Stateless Address Autoconfiguration (SLAAC) will configure their default gateway to the link-local address (e.g., `fe80::1`) of the router sending the RA.

### Device Messaging (Address Resolution & DAD)
Communication between IPv6 devices handles address resolution and duplicate checking:
1. **Neighbor Solicitation (NS) message:** 
   * **Duplicate Address Detection (DAD):** A device sends an NS message targeting its own newly generated IPv6 address. If no device responds, the address is unique.
   * **Address Resolution:** To find the MAC address of a known IPv6 destination, a device sends an NS message to the target's solicited-node multicast address.
2. **Neighbor Advertisement (NA) message:**
   * **DAD Response:** If another device is already using the queried IP address, it replies with an NA message.
   * **Address Resolution Response:** The device possessing the targeted IPv6 address replies with an NA message containing its Ethernet MAC address.

---

## 4. Network Diagnostic Tools

### Ping Test (Testing Connectivity)
The `ping` command is an IPv4 and IPv6 testing tool that uses **ICMP Echo Request** and **Echo Reply** messages to verify connectivity between hosts.
* It provides a summary that includes the success rate and the minimum, average, and maximum round-trip time (RTT) to the destination.
* If a reply is not received within the timeout period, `ping` will display a message indicating a timeout.
* *Note:* The first ping may occasionally time out if Address Resolution (ARP for IPv4, or ND for IPv6) needs to occur before the ICMP Echo Request can be dispatched.

### Traceroute (Testing the Path)
Traceroute (or `tracert` on Windows) is a tool used to map the path between two hosts, providing a list of all successful hops along the route.
* It records the round-trip time for each hop and displays an asterisk (`*`) if a hop fails to respond (indicating a lost packet or no reply).
* This information is valuable for locating problematic routers or identifying routers configured to drop ICMP packets silently.
* **How it Works:** 
  1. Traceroute sends its first sequence of messages with a TTL (or Hop Limit) of `1`.
  2. The first router receives the packet, decrements the TTL to `0`, and replies with an **ICMP Time Exceeded** message.
  3. Traceroute increments the TTL to `2` for the next sequence, which times out at the second router.
  4. This incremental TTL process continues (TTL 3, 4, 5...) until the final destination is reached or a maximum predefined hop limit is hit.
* By default, traceroute sends 3 packets per hop, giving an average idea of network latency at every stage of the path.
