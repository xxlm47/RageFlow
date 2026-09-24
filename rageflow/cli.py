import argparse
from .pipeline import RageFlow

def main():
    p = argparse.ArgumentParser(description="RageFlow multi-agent social content pipeline")
    sub = p.add_subparsers(dest="command")
    r = sub.add_parser("run")
    r.add_argument("--topic", default="relatable arguments and unpopular opinions")
    r.add_argument("--offline", action="store_true")
    r.add_argument("--count", type=int, default=5)
    args = p.parse_args()
    if args.command != "run":
        p.print_help(); return
    result = RageFlow(offline=args.offline).run(args.topic, args.count)
    for i, item in enumerate(result["posts"], 1):
        print(f"\n{i}. {item['title']}\n   {item['hook']}\n   {item['prompt']}")
