#!/usr/bin/env sh
# Install the game design skills into an agent. See: python3 tools/install.py --help
exec python3 "$(dirname "$0")/tools/install.py" "$@"
