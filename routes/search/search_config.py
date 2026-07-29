import re

MAX_SEARCH_QUERY_LEN = 80
DISALLOWED_SEARCH_CHARS = re.compile(r"[^a-zA-Z0-9\s_\-']")

SEARCH_PAGES = [
    {
        "title": "🏡 Home",
        "endpoint": "home",
        "description": "The homepage of Brawlable!",
        "keywords": ["index", "main", "start"],
    },
    {
        "title": "📧 Contact",
        "endpoint": "main.contact",
        "description": "How to contact us.",
        "keywords": ["email", "message", "help"],
    },
    {
        "title": "💁 About",
        "endpoint": "main.about",
        "description": "About this website.",
        "keywords": ["info", "company", "team"],
    },
    {
        "title": "🔒 Privacy",
        "endpoint": "main.privacy",
        "description": "Privacy policy details.",
        "keywords": ["policy", "data", "security"],
    },
    {
        "title": "📧 Support",
        "endpoint": "main.support",
        "description": "Support and assistance.",
        "keywords": ["help", "faq", "assist"],
    },
    {
        "title": "🗺️ Sitemap",
        "endpoint": "main.sitemap_page",
        "description": "Website page map.",
        "keywords": ["pages", "map", "navigation"],
    },
    {
        "title": "✍️ Attribution",
        "endpoint": "main.attribution",
        "description": "Credits and attributions.",
        "keywords": ["credits", "sources", "license"],
    },
    # Brawler Pages
    {
        "title": "🥊 Brawlers",
        "endpoint": "brawlers.brawlers",
        "description": "All brawlers in Brawl Stars.",
        "keywords": ["characters", "heroes", "fighters"],
    },
    {
        "title": "🟢 Rare Brawlers",
        "endpoint": "brawlers.rare",
        "description": "Rare rarity brawlers.",
        "keywords": ["brawlers", "rare", "rarity"],
    },
    {
        "title": "🔵 Super Rare Brawlers",
        "endpoint": "brawlers.super_rare",
        "description": "Super Rare rarity brawlers.",
        "keywords": ["brawlers", "super rare", "rarity"],
    },
    {
        "title": "🟣 Epic Brawlers",
        "endpoint": "brawlers.epic",
        "description": "Epic rarity brawlers.",
        "keywords": ["brawlers", "epic", "rarity"],
    },
    {
        "title": "🔴 Mythic Brawlers",
        "endpoint": "brawlers.mythic",
        "description": "Mythic rarity brawlers.",
        "keywords": ["brawlers", "mythic", "rarity"],
    },
    {
        "title": "🟡 Legendary Brawlers",
        "endpoint": "brawlers.legendary",
        "description": "Legendary rarity brawlers.",
        "keywords": ["brawlers", "legendary", "rarity"],
    },
    {
        "title": "👑 Ultra Legendary Brawlers",
        "endpoint": "brawlers.ultra_legendary",
        "description": "Ultra Legendary rarity brawlers.",
        "keywords": ["brawlers", "ultra legendary", "rarity"],
    },
    # Gamemode Pages
    {
        "title": "⭐️ Bounty",
        "endpoint": "gamemodes.bounty",
        "description": "Bounty game mode.",
        "keywords": ["gamemode", "stars", "kills"],
    },
    {
        "title": "⚽️ Brawl Ball",
        "endpoint": "gamemodes.brawl_ball",
        "description": "Brawl Ball game mode.",
        "keywords": ["gamemode", "3v3", "5v5", "ball"],
    },
    {
        "title": "💎 Gem Grab",
        "endpoint": "gamemodes.gem_grab",
        "description": "Gem Grab game mode.",
        "keywords": ["gamemode", "gems", "grab", "3v3"],
    },
    {
        "title": "💰 Heist",
        "endpoint": "gamemodes.heist",
        "description": "Heist game mode.",
        "keywords": ["gamemode", "safe", "3v3"],
    },
    {
        "title": "⭕️ Hot Zone",
        "endpoint": "gamemodes.hot_zone",
        "description": "Hot Zone game mode.",
        "keywords": ["gamemode", "zone", "3v3"],
    },
    {
        "title": "🧙‍♂️ Showdown",
        "endpoint": "gamemodes.showdown",
        "description": "Showdown game mode.",
        "keywords": ["gamemode", "solo", "duo", "trio"],
    },
    {
        "title": "🔫 Knockout",
        "endpoint": "gamemodes.knockout",
        "description": "Knockout game mode.",
        "keywords": ["gamemode", "3v3", "team", "5v5"],
    },
    {
        "title": "👥 Wipeout",
        "endpoint": "gamemodes.wipeout",
        "description": "Wipeout game mode.",
        "keywords": ["gamemode", "team", "5v5"],
    },
    # Individual Brawlers
    {
        "title": "🚀 Brock Guide",
        "endpoint": "guides_brawlers.rare_brawler_guide",
        "url_values": {"name": "brock"},
        "description": "A guide for playing Brock.",
        "keywords": ["brock", "rare", "brawler", "guide"],
    },
    {
        "title": "🐂 Bull Guide",
        "endpoint": "guides_brawlers.rare_brawler_guide",
        "url_values": {"name": "bull"},
        "description": "A guide for playing Bull.",
        "keywords": ["bull", "rare", "brawler", "guide"],
    },
]
