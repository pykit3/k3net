# k3net

[![Action-CI](https://github.com/pykit3/k3net/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3net/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3net/badge/?version=stable)](https://k3net.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3net)](https://pypi.org/project/k3net)

Network utilities for IP address detection and classification. Get host IP addresses, classify public/private IPs.

k3net is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3net
```

## Quick Start

```python
import k3net

# Get host IP addresses
ips = k3net.get_host_ip4()
print(ips)  # ['192.168.1.100', '10.0.0.1']

# Check if IP is public or private
print(k3net.is_pub('8.8.8.8'))   # True
print(k3net.is_inn('10.0.0.1'))  # True

# Classify IP
print(k3net.ip_class('192.168.1.1'))  # 'INN'
print(k3net.ip_class('8.8.8.8'))      # 'PUB'

# Convert IP to number and back
num = k3net.ip_to_num('192.168.1.1')
ip = k3net.num_to_ip(num)
```

## API Reference

::: k3net

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
