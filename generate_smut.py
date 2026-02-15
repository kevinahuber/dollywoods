#!/usr/bin/env python3
"""Generate the Wyvern's Library fantasy smut section authors for DOLLYWOODS."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_site import (
    generate_artist_page, generate_story_page, generate_profile_svg,
    BASE_DIR, IMG_DIR
)

SMUT_AUTHORS = [
    {
        "slug": "velvet-thornrose",
        "name": "Velvet Thornrose",
        "location": "New Orleans, Louisiana, USA",
        "member_since": "May 1999",
        "media": "Fantasy Romance &amp; Erotica",
        "influences": "Anne Rice, Jacqueline Carey, Southern Gothic tradition, perfume advertisements",
        "bio": "Well hey there, darlin'. I write stories about beautiful, dangerous people doin' beautiful, dangerous things to each other in fantastical settings. My specialty is vampire romance set in a fantasy version of New Orleans where the Spanish moss drips with magic and every masked ball could be your last. Reader discretion is advised, but honey, if you're here, I reckon you've got plenty of discretion already. Currently working on my magnum opus, 'The Crimson Covenant' series.",
        "total_images": 0,
        "total_comments": 187,
        "gallery_created": "May 13, 1999",
        "last_updated": "July 14, 2002",
        "is_writer": True,
        "section": "wyverns-library",
        "stories": [
            {"slug": "velvet-crimson-covenant", "title": "The Crimson Covenant: Blood and Magnolias", "genre": "Vampire Romance", "words": "34,200", "status": "Chapters 1-12 (In Progress)", "date": "Jul 14, 2002", "badge": "UPDATED!", "desc": "When mortal herbalist Camille stumbles into the court of the Vampire Lord of the Bayou, she discovers that the line between predator and prey is thinner than silk &mdash; and considerably more entangling. A lush, steamy tale of forbidden desire set in a fantasy New Orleans dripping with Spanish moss and dark magic."},
            {"slug": "velvet-fae-bargain", "title": "A Fae Bargain (Explicit)", "genre": "Fae Erotica", "words": "8,600", "status": "Complete", "date": "Jun 20, 2002", "badge": "", "desc": "A mortal woman makes a deal with a fae lord at a Midsummer revel. The terms are... unconventional. What unfolds is a night of glamour, enchantment, and increasingly creative interpretations of fairy tale logic. Explicit content. You have been warned, sugar."},
            {"slug": "velvet-siren-song", "title": "The Siren's Song", "genre": "Fantasy Romance", "words": "5,100", "status": "Complete", "date": "May 8, 2002", "badge": "", "desc": "A sailor who is immune to siren song finds herself drawn to a siren who has never failed to enchant. When the magic doesn't work, something far more dangerous takes its place: genuine attraction. Set on a fantasy version of the Gulf Coast."},
        ],
    },
    {
        "slug": "duke-ravencroft",
        "name": "Duke Ravencroft",
        "location": "Brighton, England, UK",
        "member_since": "August 2000",
        "media": "Dark Fantasy Romance",
        "influences": "Storm Constantine, Tanith Lee, Poppy Z. Brite, Gothic architecture",
        "bio": "I write darkly romantic fantasy about complicated people in complicated situations, often involving sorcerers, demons, and morally ambiguous bargains sealed with more than a handshake. My stories explore power dynamics, obsession, and desire in settings where magic amplifies every emotion to its breaking point. Not for the faint of heart. Absolutely for the queer of heart.",
        "total_images": 0,
        "total_comments": 142,
        "gallery_created": "August 8, 2000",
        "last_updated": "July 11, 2002",
        "is_writer": True,
        "section": "wyverns-library",
        "stories": [
            {"slug": "duke-demon-pact", "title": "The Demon's Pact", "genre": "Dark Romance", "words": "18,900", "status": "Chapters 1-6 (In Progress)", "date": "Jul 11, 2002", "badge": "UPDATED!", "desc": "A disgraced sorcerer summons a demon to restore his power. The demon agrees &mdash; for a price that has nothing to do with souls and everything to do with surrender. A slow-burn descent into obsession between two beings who should absolutely not be trusted with each other."},
            {"slug": "duke-shadow-court", "title": "Nights at the Shadow Court (Explicit)", "genre": "Gothic Erotica", "words": "12,400", "status": "Complete", "date": "Jun 5, 2002", "badge": "", "desc": "In a decadent court of shadow fae, a mortal ambassador discovers that diplomacy takes many forms &mdash; some of which aren't in any protocol handbook. Five interconnected stories of intrigue, seduction, and glamour in a court where nothing is as it seems."},
            {"slug": "duke-warlock-price", "title": "The Warlock's Price", "genre": "Fantasy Romance", "words": "7,200", "status": "Complete", "date": "Apr 22, 2002", "badge": "", "desc": "Two rival warlocks, trapped together in a magical storm, discover that the tension between them was never really about professional jealousy. A enemies-to-lovers tale with actual fireballs and a very inconvenient truth potion."},
        ],
    },
    {
        "slug": "sable-moonwhisper",
        "name": "Sable Moonwhisper",
        "location": "Portland, Oregon, USA",
        "member_since": "February 2001",
        "media": "Romantic Fantasy &amp; Erotica",
        "influences": "Mercedes Lackey, Marion Zimmer Bradley, Pacific Northwest mythology, hot springs",
        "bio": "I believe fantasy erotica is a legitimate art form and I will die on that hill! My stories feature diverse characters in richly built fantasy worlds where intimacy is treated as a form of magic in its own right. Shapeshifters, druids, elemental mages &mdash; turns out magical abilities make everything more interesting. I write with care, consent is always central to my stories, and I firmly believe love scenes deserve the same craft as battle scenes.",
        "total_images": 0,
        "total_comments": 118,
        "gallery_created": "February 14, 2001",
        "last_updated": "July 9, 2002",
        "is_writer": True,
        "section": "wyverns-library",
        "stories": [
            {"slug": "sable-shapeshifter-heart", "title": "The Shapeshifter's Heart", "genre": "Romantic Fantasy", "words": "26,400", "status": "Chapters 1-9 (In Progress)", "date": "Jul 9, 2002", "badge": "NEW!", "desc": "A wolf-shifter and a hawk-shifter from rival clans are forced into a diplomatic marriage to prevent war. The ceremony requires a magical bonding ritual that neither of them is prepared for &mdash; emotionally or otherwise. Slow burn to wildfire."},
            {"slug": "sable-hot-springs", "title": "The Enchanted Hot Springs (Explicit)", "genre": "Fantasy Erotica", "words": "6,800", "status": "Complete", "date": "Jun 14, 2002", "badge": "", "desc": "A traveling healer discovers a hidden hot spring in the mountains that grants visions of your heart's deepest desire. When a mysterious ranger arrives at the same spring, the visions become considerably more vivid. And mutual. Steam in every sense of the word."},
            {"slug": "sable-druid-rite", "title": "The Druid's Beltane Rite", "genre": "Fantasy Erotica", "words": "4,200", "status": "Complete", "date": "Apr 30, 2002", "badge": "", "desc": "Two druids perform the ancient Beltane fertility rite to renew the land's magic. The ritual requires absolute sincerity, and as the magic builds, so does everything else. Tender, magical, and explicit. Set in a fantasy Pacific Northwest old-growth forest."},
        ],
    },
    {
        "slug": "baron-silktongue",
        "name": "Baron Silktongue",
        "location": "Vienna, Austria",
        "member_since": "November 2001",
        "media": "Fantasy Erotica &amp; Satire",
        "influences": "Terry Pratchett, Boccaccio's Decameron, Mozart's operas, bawdy medieval poetry",
        "bio": "Guten Tag! I write humorous fantasy erotica because someone has to, and I happen to be very good at it. My stories are equal parts steamy and funny, set in a fantasy world that doesn't take itself too seriously. If Terry Pratchett wrote bodice-rippers, they might read something like my work (and I say that with the deepest respect and absolutely no authority). Currently writing the 'Misadventures' series about a hapless bard whose romantic escapades keep accidentally saving the kingdom.",
        "total_images": 0,
        "total_comments": 94,
        "gallery_created": "November 1, 2001",
        "last_updated": "July 13, 2002",
        "is_writer": True,
        "section": "wyverns-library",
        "stories": [
            {"slug": "baron-bard-misadventures", "title": "The Bard's Misadventures: An Indecent Overture", "genre": "Humorous Erotica", "words": "22,100", "status": "Chapters 1-8 (In Progress)", "date": "Jul 13, 2002", "badge": "UPDATED!", "desc": "Fidelio the bard has a gift for music, a weakness for beautiful people of all descriptions, and an absolute talent for ending up in the wrong bedchamber at the worst possible moment. When his latest romantic entanglement accidentally prevents an assassination, the queen herself takes an interest in his... talents."},
            {"slug": "baron-dragon-hoard", "title": "The Dragon's Hoard of Lingerie", "genre": "Humorous Fantasy", "words": "3,400", "status": "Complete", "date": "Jun 1, 2002", "badge": "", "desc": "A knight sent to slay a dragon discovers its hoard isn't gold &mdash; it's an enormous collection of stolen undergarments from every kingdom in the realm. The dragon is deeply embarrassed. The knight is deeply confused. Neither of them expected to bond over this."},
            {"slug": "baron-love-potion", "title": "Love Potion Number Nein", "genre": "Romantic Comedy", "words": "5,700", "status": "Complete", "date": "Apr 15, 2002", "badge": "", "desc": "An alchemist's love potion goes hilariously wrong at a royal banquet, causing everyone to fall desperately in love with the nearest piece of furniture. In the chaos, the alchemist and his rival discover their feelings for each other are entirely unenchanted."},
        ],
    },
]

def main():
    print("Generating Wyvern's Library fantasy romance/erotica section...")
    file_count = 0

    for author in SMUT_AUTHORS:
        slug = author["slug"]

        # Generate profile SVG
        profile_svg = generate_profile_svg(slug)
        with open(os.path.join(IMG_DIR, f"{slug}-profile.svg"), "w") as f:
            f.write(profile_svg)
        file_count += 1

        # Generate author page
        author_page = generate_artist_page(author)
        with open(os.path.join(BASE_DIR, f"{slug}.html"), "w") as f:
            f.write(author_page)
        file_count += 1

        # Generate story pages
        for story in author.get("stories", []):
            story_page = generate_story_page(author, story)
            with open(os.path.join(BASE_DIR, f"{story['slug']}.html"), "w") as f:
                f.write(story_page)
            file_count += 1

    print(f"Generated {file_count} files for {len(SMUT_AUTHORS)} authors!")

if __name__ == "__main__":
    main()
