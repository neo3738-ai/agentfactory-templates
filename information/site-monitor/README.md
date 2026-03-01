# Website Monitor

Monitor a website for changes and get notified

## Pipeline

Fetch Page -> Detect Changes

## Agents

1. **Web Fetcher** (fetcher): Fetch the current content of a web page
2. **Change Detector** (analyst): Compare fetched content against previous state and report changes

**Schedule:** `0 */4 * * *`

## Usage

Use this template from the Agentfactory Home tab or install it from the Marketplace.
