*This activity has been created as part of the 42 curriculum by oalabed.*

# Born2beRoot

## Description

Born2beRoot is a system administration project from the 42 curriculum. The objective is to create and configure a secure Linux server running inside a virtual machine while following strict security and administration requirements.

The project introduces fundamental Linux system administration concepts including:

- Virtualization
- Disk partitioning with LVM
- User and group management
- SSH configuration
- Firewall configuration
- Password policies
- Sudo configuration
- Security modules
- Bash scripting
- Cron jobs
- System monitoring

The final result is a minimal, secure server that can be remotely administered and monitored.

---

# Project Description

## Operating System Choice

I chose **Debian Stable**.

### Advantages

- Excellent documentation
- Very stable
- Huge software repository
- Beginner friendly
- Uses APT package manager
- Large community support

### Disadvantages

- Slightly older package versions
- Less enterprise-oriented than Rocky Linux

---

# Debian vs Rocky Linux

| Debian | Rocky Linux |
|---------|-------------|
| Community driven | Enterprise distribution |
| Uses APT | Uses DNF/YUM |
| AppArmor by default | SELinux by default |
| Easier for beginners | Preferred in enterprise environments |
| Large software repositories | RHEL compatible |

---

# AppArmor vs SELinux

## AppArmor

Advantages

- Easier to configure
- Path-based security
- Simpler profiles
- Better for beginners

Disadvantages

- Less granular
- Mostly used on Debian/Ubuntu

---

## SELinux

Advantages

- Label-based security
- Extremely powerful
- Fine-grained access control
- Enterprise standard

Disadvantages

- More difficult to configure
- Harder to troubleshoot

---

# UFW vs firewalld

## UFW

Advantages

- Very easy to use
- Simple command syntax
- Ideal for Debian

Disadvantages

- Fewer advanced features

---

## firewalld

Advantages

- Dynamic configuration
- Zones
- Rich rules
- Enterprise ready

Disadvantages

- Slightly more complex

---

# VirtualBox vs UTM

## VirtualBox

Advantages

- Free
- Cross-platform
- Mature
- Well documented

Disadvantages

- Intel virtualization focused

---

## UTM

Advantages

- Native Apple Silicon support
- Based on QEMU
- Better for macOS M-series

Disadvantages

- Mostly useful only on macOS

---

# System Architecture

- Operating System: Debian Stable
- Virtualization: VirtualBox
- Kernel: Linux
- Hostname: <oalabed42>

---

# Partition Layout

This project uses encrypted LVM partitions.

Example:

```
/boot
/
/home
/var
/srv
/tmp
/var/log
```

Advantages of LVM

- Flexible resizing
- Easier storage management
- Better administration
- Snapshot capability

---

# Security Configuration

## SSH

- Running on port 4242
- Root login disabled
- Password authentication enabled (or key authentication if configured)

---

## Firewall

Using UFW

Allowed ports

- 4242/tcp

Everything else is denied.

---

## Password Policy

Configured using PAM.

Rules

- Minimum length: 10
- Uppercase required
- Lowercase required
- Number required
- Username forbidden
- Maximum 3 repeated characters
- Password expires every 30 days
- Minimum 2 days before changing
- Warning 7 days before expiration

---

## Sudo Configuration

Configured with:

- 3 authentication attempts
- Custom error message
- TTY enabled
- Restricted secure path
- All commands logged
- Logs stored in

```
/var/log/sudo/
```

---

# Users

Created users

- root
- <your_login>

Groups

- sudo
- user42

---

# Monitoring Script

A Bash script named **monitoring.sh** is executed automatically every 10 minutes using cron.

The script displays:

- Architecture
- Kernel version
- Physical CPUs
- Virtual CPUs
- RAM usage
- Disk usage
- CPU load
- Last boot
- LVM status
- TCP connections
- Logged users
- IP address
- MAC address
- Number of sudo commands

The information is broadcast to every terminal using:

```
wall
```

---

# Instructions

## Requirements

- VirtualBox
- Debian Stable ISO
- Internet connection

---

## Installation

1. Create a new virtual machine.
2. Install Debian Stable.
3. Configure encrypted LVM.
4. Install OpenSSH Server.
5. Configure SSH on port 4242.
6. Install and configure UFW.
7. Configure password policies.
8. Configure sudo.
9. Create user and groups.
10. Install monitoring script.
11. Configure cron.
12. Reboot and verify everything.

---

## Running the Monitoring Script

Manual execution

```bash
bash monitoring.sh
```

Cron automatically executes it every 10 minutes.

---

# Verification Checklist

✔ Debian Stable

✔ VirtualBox

✔ No graphical interface

✔ AppArmor enabled

✔ Encrypted LVM

✔ SSH on port 4242

✔ Root login disabled

✔ UFW active

✔ Only port 4242 open

✔ Hostname ends with 42

✔ Strong password policy

✔ Correct sudo configuration

✔ User belongs to sudo and user42

✔ Monitoring script works

✔ Broadcast every 10 minutes

---

# Useful Commands

Check SSH

```bash
sudo systemctl status ssh
```

Check Firewall

```bash
sudo ufw status
```

Check AppArmor

```bash
aa-status
```

Check LVM

```bash
lsblk
```

Check Cron

```bash
crontab -l
```

Check Password Expiration

```bash
chage -l <username>
```

Check Groups

```bash
groups <username>
```

---

# Resources

Official Documentation

- Debian Documentation
- Debian Wiki
- OpenSSH Documentation
- UFW Documentation
- AppArmor Documentation
- LVM HOWTO
- PAM Documentation
- Cron Documentation
- Bash Manual

Useful Tutorials

- DigitalOcean Linux Tutorials
- Linux Journey
- The Linux Documentation Project

---

# AI Usage

AI was used only as a learning assistant for:

- Understanding Linux concepts
- Explaining AppArmor and SELinux
- Comparing Debian and Rocky Linux
- Improving documentation structure
- Reviewing shell scripts
- Learning Bash syntax

All configuration, installation, testing, debugging, and implementation were performed manually.

---

# Conclusion

Born2beRoot provides practical experience in Linux system administration, virtualization, server security, automation, and Bash scripting. Completing this project builds a solid foundation for future DevOps, cybersecurity, and infrastructure-related work.
