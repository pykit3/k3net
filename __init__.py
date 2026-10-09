from .net import (
    INN,
    LOCALHOST,
    PUB,
    InvalidIP4,
    InvalidIP4Number,
    IPUnreachable,
    NetworkError,
    choose_by_idc,
    choose_by_regex,
    choose_inn,
    choose_ips,
    choose_pub,
    get_host_devices,
    get_host_ip4,
    ip_class,
    ip_to_num,
    ips_prefer,
    is_inn,
    is_ip4,
    is_ip4_loopback,
    is_pub,
    num_to_ip,
    parse_ip_regex_str,
)

__all__ = [
    "INN",
    "LOCALHOST",
    "PUB",
    "IPUnreachable",
    "InvalidIP4",
    "InvalidIP4Number",
    "NetworkError",
    "choose_by_idc",
    "choose_by_regex",
    "choose_inn",
    "choose_ips",
    "choose_pub",
    "get_host_devices",
    "get_host_ip4",
    "ip_class",
    "ip_to_num",
    "ips_prefer",
    "is_inn",
    "is_ip4",
    "is_ip4_loopback",
    "is_pub",
    "num_to_ip",
    "parse_ip_regex_str",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3net")
