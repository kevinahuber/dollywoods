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
        "location": "Lewisburg, West Virginia, USA",
        "member_since": "May 1999",
        "media": "Fantasy Romance &amp; Erotica",
        "influences": "Appalachian ghost stories, Anne Rice, granny witch traditions, moonshine, moth imagery",
        "bio": "I'm a girl from the Greenbrier Valley who writes stories hotter than a coal stove in January. My specialty is Mothman romance &mdash; and before you laugh, honey, you ain't read my version. In my stories, the Mothman ain't just a harbinger of doom, he's a harbinger of doom and desire. I grew up hearin' my meemaw's stories about the strange things that happen in these mountains after dark, and I reckon the line between bein' scared and bein' excited is thinner than a spider's thread. Currently workin' on 'The Crimson Covenant,' a vampire saga set in the hollers.",
        "total_images": 0,
        "total_comments": 187,
        "gallery_created": "May 13, 1999",
        "last_updated": "July 14, 2002",
        "is_writer": True,
        "section": "wyverns-library",
        "stories": [
            {"slug": "velvet-crimson-covenant", "title": "The Crimson Covenant: Blood in the Holler", "genre": "Vampire Romance", "words": "34,200", "status": "Chapters 1-12 (In Progress)", "date": "Jul 14, 2002", "badge": "UPDATED!", "desc": "When herbalist Jessamine follows a strange red light into the abandoned mine above Lewisburg, she stumbles into the court of a vampire lord who's been sleepin' under the Appalachian hills since before the first settlers crossed the mountains. He's ancient, he's dangerous, and he smells like cedar and old moonshine. A lush, steamy tale of forbidden desire set deep in the West Virginia hollers."},
            {"slug": "velvet-fae-bargain", "title": "The Mothman's Bride (Explicit)", "genre": "Cryptid Erotica", "words": "8,600", "status": "Complete", "date": "Jun 20, 2002", "badge": "", "desc": "On the anniversary of the Silver Bridge collapse, a woman in Point Pleasant sees those red eyes watchin' her from the TNT Area. But instead of runnin', she follows. What she finds ain't a monster &mdash; it's somethin' far more complicated, far more beautiful, and far more hungry. The Mothman ain't what you think he is, darlin'. Explicit content."},
            {"slug": "velvet-siren-song", "title": "The Wampus Cat's Lover", "genre": "Fantasy Romance", "words": "5,100", "status": "Complete", "date": "May 8, 2002", "badge": "", "desc": "A Cherokee woman cursed into the shape of a six-legged panther &mdash; the Wampus Cat &mdash; can only return to human form in the arms of someone who truly sees her. A lonely fiddle player in the Smokies hears somethin' howlin' harmony with his music. A tender, aching romance about seein' past the monster to the person underneath."},
        ],
    },
    {
        "slug": "duke-ravencroft",
        "name": "Duke Ravencroft",
        "location": "Asheville, North Carolina, USA",
        "member_since": "August 2000",
        "media": "Dark Fantasy Romance",
        "influences": "Appalachian granny magic, queer Southern Gothic, Manly Wade Wellman, haunted hollers",
        "bio": "I'm a queer writer from the Blue Ridge who writes darkly romantic fantasy about the strange things that happen when the mist rolls in and the old magic wakes up. My stories are full of shape-shifters, haints, and morally complicated conjure-folk who settle their debts in ways that'd make a preacher blush. I believe Appalachia is the most magical landscape in America, and I write the stories these mountains whisper to me at three in the mornin'. Not for the faint of heart. Absolutely for the queer of heart.",
        "total_images": 0,
        "total_comments": 142,
        "gallery_created": "August 8, 2000",
        "last_updated": "July 11, 2002",
        "is_writer": True,
        "section": "wyverns-library",
        "stories": [
            {"slug": "duke-demon-pact", "title": "The Conjure Man's Price", "genre": "Dark Romance", "words": "18,900", "status": "Chapters 1-6 (In Progress)", "date": "Jul 11, 2002", "badge": "UPDATED!", "desc": "A disgraced conjure man on Bald Mountain summons somethin' from the old dark to restore his power. The thing that answers ain't a demon exactly &mdash; it's older than demons, shaped like a man made of shadow and foxfire, and its price has nothin' to do with souls and everything to do with surrender. A slow-burn descent into obsession set in the deepest hollers of the Blue Ridge."},
            {"slug": "duke-shadow-court", "title": "Nights in the Haint Holler (Explicit)", "genre": "Gothic Erotica", "words": "12,400", "status": "Complete", "date": "Jun 5, 2002", "badge": "", "desc": "A wanderin' musician stumbles into a holler that ain't on any map, where the dead hold court every full moon. The haints are beautiful, the moonshine flows like water, and the fiddler discovers that some dances last 'til dawn and leave marks that don't fade. Five interconnected stories of spectral seduction in the haunted mountains."},
            {"slug": "duke-warlock-price", "title": "The Sasquatch Whisperer", "genre": "Fantasy Romance", "words": "7,200", "status": "Complete", "date": "Apr 22, 2002", "badge": "", "desc": "Two rival cryptid researchers, trapped together in a cabin during a Blue Ridge blizzard, discover that the tension between them was never really about who saw Bigfoot first. When somethin' large and gentle leaves gifts on their porch each mornin', they realize the mountain itself might be playin' matchmaker. Enemies-to-lovers with a Sasquatch wingman."},
        ],
    },
    {
        "slug": "sable-moonwhisper",
        "name": "Sable Moonwhisper",
        "location": "Hot Springs, North Carolina, USA",
        "member_since": "February 2001",
        "media": "Romantic Fantasy &amp; Erotica",
        "influences": "Appalachian hot springs, shape-shifter folklore, Cherokee mythology, herbalism, firefly season",
        "bio": "I live in Hot Springs, NC &mdash; yes, the town with the actual hot springs &mdash; and if you don't think soakin' in mineral water under a million stars inspires romantic fantasy, then honey, you ain't been soakin' right. I write stories where the magic of these old mountains makes everything more intense: shape-shifters who run the ridgelines, granny witches whose love spells actually work, and encounters with creatures from Cherokee legend that change you in ways you didn't expect. Consent is always central to my stories, and I believe love scenes deserve the same craft as any other magic.",
        "total_images": 0,
        "total_comments": 118,
        "gallery_created": "February 14, 2001",
        "last_updated": "July 9, 2002",
        "is_writer": True,
        "section": "wyverns-library",
        "stories": [
            {"slug": "sable-shapeshifter-heart", "title": "The Shapeshifter's Heart", "genre": "Romantic Fantasy", "words": "26,400", "status": "Chapters 1-9 (In Progress)", "date": "Jul 9, 2002", "badge": "NEW!", "desc": "A woman who can shift into a red fox and a man who runs with the wolves are from feudin' mountain clans. When the elders arrange a marriage to end the blood feud, the bondin' ritual under the full moon on Max Patch requires them to shift together &mdash; and trust each other in their most vulnerable forms. Slow burn to wildfire, set along the Appalachian Trail."},
            {"slug": "sable-hot-springs", "title": "The Enchanted Springs (Explicit)", "genre": "Fantasy Erotica", "words": "6,800", "status": "Complete", "date": "Jun 14, 2002", "badge": "", "desc": "A granny witch guards a secret hot spring deep in the Pisgah National Forest that shows you visions of your heart's truest desire. When a lonesome hiker stumbles in at the same time as a mysterious woman with owl eyes, the visions get real vivid, real mutual, and real steamy. In every sense of the word."},
            {"slug": "sable-druid-rite", "title": "The Beltane Fire on Roan Mountain (Explicit)", "genre": "Fantasy Erotica", "words": "4,200", "status": "Complete", "date": "Apr 30, 2002", "badge": "", "desc": "Two mountain witches perform the old Beltane fire ritual on the bald of Roan Mountain to wake the rhododendrons and bring the spring. The ritual requires absolute sincerity, bare feet on cold earth, and a willin'ness to let the mountain's magic flow through you. Tender, wild, and explicit. Set among the natural rhododendron gardens at 6,000 feet."},
        ],
    },
    {
        "slug": "baron-silktongue",
        "name": "Baron Silktongue",
        "location": "Floyd, Virginia, USA",
        "member_since": "November 2001",
        "media": "Fantasy Erotica &amp; Satire",
        "influences": "Jack Tales, bawdy Appalachian fiddle tunes, tall tales, the Floyd Country Store, moonshine culture",
        "bio": "Howdy, I'm the Baron, and I write the kind of stories you'd hear at the back table of the Floyd Country Store if the old-timers had a few too many and started tellin' tales about the time Cousin Junebug got seduced by a Flatwoods Monster. My stories are equal parts steamy and hilarious, set in a fantasy Appalachia where the cryptids are frisky, the moonshine is enchanted, and the fiddle music makes you do things you wouldn't normally do. If the Jack Tales had an adults-only section, this would be it.",
        "total_images": 0,
        "total_comments": 94,
        "gallery_created": "November 1, 2001",
        "last_updated": "July 13, 2002",
        "is_writer": True,
        "section": "wyverns-library",
        "stories": [
            {"slug": "baron-bard-misadventures", "title": "The Fiddler's Misadventures: A Flatwoods Fling", "genre": "Humorous Erotica", "words": "22,100", "status": "Chapters 1-8 (In Progress)", "date": "Jul 13, 2002", "badge": "UPDATED!", "desc": "Jebediah the fiddle player has a gift for music, a weakness for beautiful strangers, and an absolute talent for endin' up in the wrong holler at the worst possible moment. When his latest romantic entanglement with a suspiciously attractive Flatwoods Monster accidentally prevents a Mothman prophecy from comin' true, the Granny Witch Council takes an interest in his... talents."},
            {"slug": "baron-dragon-hoard", "title": "The Snallygaster's Unmentionables", "genre": "Humorous Fantasy", "words": "3,400", "status": "Complete", "date": "Jun 1, 2002", "badge": "", "desc": "A hunter in the Blue Ridge sent to track the fearsome Snallygaster discovers its nest ain't full of bones &mdash; it's full of stolen long johns, petticoats, and bloomers from every clothesline in three counties. The Snallygaster is deeply embarrassed. The hunter is deeply confused. Neither of 'em expected to become friends over this."},
            {"slug": "baron-love-potion", "title": "Love Potion Number Shine", "genre": "Romantic Comedy", "words": "5,700", "status": "Complete", "date": "Apr 15, 2002", "badge": "", "desc": "A mountain granny's love-potion moonshine goes hilariously wrong at the Floyd Jamboree, causin' everyone to fall desperately in love with the nearest musical instrument. In the chaos, the granny's two feudin' grandchildren &mdash; one who swears they saw Bigfoot, one who says it was just a bear &mdash; discover their feelings for each other are entirely unenchanted."},
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
