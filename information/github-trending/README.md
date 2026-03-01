# GitHub Trending Digest

Get a digest of trending GitHub repositories

## Pipeline

Fetch Trending -> Write Digest

## Agents

1. **GH Scanner** (researcher): Fetch trending GitHub repositories
2. **Trend Reporter** (writer): Write a trending repos digest

**Schedule:** `0 17 * * *`

## Usage

Use this template from the Agentfactory Home tab or install it from the Marketplace.
