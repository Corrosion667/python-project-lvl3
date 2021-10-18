#!/usr/bin/env python3
"""This program downloads a page from the network."""
import argparse

from page_loader.download import DEFAULT_PATH, download

SUCCESS = "Page was successfully downloaded into '{0}'"


def main():
    """Execute the page loader."""
    parser = argparse.ArgumentParser(description='Download web page')
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=DEFAULT_PATH,
        help='select folder where to download the page',
    )
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    path = download(args.url, args.output)
    print(SUCCESS.format(path))


if __name__ == '__main__':
    main()
