#!/usr/bin/env python3
"""Generate cryptid-focused artist pages for DOLLYWOODS."""

# Import all the generation functions from the main script
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_site import (
    generate_artist_page, generate_artwork_page,
    generate_creature_svg, generate_thumbnail_svg, generate_profile_svg,
    BASE_DIR, IMG_DIR
)

CRYPTID_ARTISTS = [
    {
        "slug": "mothman-molly",
        "name": "Mothman Molly",
        "location": "Point Pleasant, West Virginia, USA",
        "member_since": "October 1998",
        "media": "Charcoal, Pastel, Digital",
        "influences": "John Keel, my granny's porch stories, the TNT Area at night, old Polaroids of things that shouldn't be there",
        "bio": "Well now, I live ten minutes from where the Silver Bridge used to stand, and I been drawin' the Mothman since before I could spell his name right. My meemaw saw them red eyes back in '66 and she ain't never been the same &mdash; said they was beautiful and terrible all at once, like starin' into a coal fire that stares back. I draw what the mountains show me: the strange critters that live in the hollers, the things that watch from the ridgelines when the fog rolls in. Charcoal's my main thing 'cause it's dark like the creatures I draw. Not sayin' I seen him personally. Not sayin' I ain't, neither.",
        "total_images": 19,
        "total_comments": 104,
        "gallery_created": "October 31, 1998",
        "last_updated": "July 14, 2002",
        "artworks": [
            {"slug": "molly-mothman-bridge", "title": "Mothman on the Silver Bridge", "medium": "Charcoal &amp; Red Pastel", "date": "Jul 14, 2002", "badge": "NEW!", "color": "#3a2233", "desc": "Lord have mercy, this one gives me chills every time I look at it. A towerin' winged figure with blazin' red eyes perched on the cables of the Silver Bridge, back before it fell. The Ohio River churns black as coal dust below. I done it in charcoal with just his eyes in blood-red pastel 'cause that's how folks described it &mdash; darkness with two burnin' lights. My meemaw cried when she saw this one."},
            {"slug": "molly-flatwoods-monster", "title": "The Braxton County Visitor", "medium": "Pastel &amp; Digital", "date": "Jun 22, 2002", "badge": "", "color": "#224422", "desc": "Now this here's the Flatwoods Monster, spotted up in Braxton County back in '52. Hoverin' above a misty West Virginia hillside with its ace-of-spades head glowin' green as a firefly, long clawed fingers reachin' out from what looks like a pleated metal skirt. A group of young'uns are runnin' down the path hollerin' bloody murder. Can't say I blame 'em none."},
            {"slug": "molly-wampus-cat", "title": "The Wampus Cat Prowls", "medium": "Charcoal &amp; Pastel", "date": "May 30, 2002", "badge": "", "color": "#554433", "desc": "Six legs, amber eyes that glow like lanterns, and a growl that'll curdle the milk in your icebox from half a mile away. That's the Wampus Cat, stalkin' through moonlit laurel thickets up on the mountain. Cherokee folks say it's a woman cursed for spyin' on sacred rituals. I spent three weeks gettin' the fur right &mdash; every hair drawn by hand, Lord help me."},
            {"slug": "molly-mothman-prophecy", "title": "Red Eyes Over the Holler", "medium": "Digital &amp; Charcoal", "date": "Apr 15, 2002", "badge": "", "color": "#2a1122", "desc": "A wide view of a misty Appalachian holler at twilight, the kind of valley where sound carries funny and the fog has a mind of its own. Two enormous red eyes glow from the ridgeline above a little cluster of houses. Every window in the holler is dark 'cept one, where somebody's standin' at the glass, lookin' up. Somethin's comin'. Somethin' always is."},
        ],
    },
    {
        "slug": "sasquatch-sam",
        "name": "Sasquatch Sam",
        "location": "Marlinton, West Virginia, USA",
        "member_since": "March 2000",
        "media": "Oils, Gouache",
        "influences": "The Monongahela National Forest, my papaw's huntin' stories, every blurry photo ever taken in Pocahontas County",
        "bio": "Howdy, I'm Sam and I paint Bigfoot. Now I know what you're thinkin', but hear me out: I grew up in Pocahontas County, which has had more Sasquatch sightin's per square mile than dang near anywhere east of the Mississippi. My papaw saw one crossin' Cranberry River in 1971, big as a hay bale and twice as hairy, and he weren't the type to make things up. I paint these mountains the way they really are &mdash; ancient, deep, full of mist and mystery &mdash; and then I put somethin' in 'em that most folks ain't brave enough to look for. Every paintin' is based on an actual sightin' report from right here in the Appalachian hills.",
        "total_images": 14,
        "total_comments": 78,
        "gallery_created": "March 15, 2000",
        "last_updated": "July 10, 2002",
        "artworks": [
            {"slug": "sam-sasquatch-creek", "title": "Crossin' at Cranberry River", "medium": "Oils", "date": "Jul 10, 2002", "badge": "NEW!", "color": "#3a4a2a", "desc": "Based on my papaw's sightin'. A massive, shaggy figure mid-stride crossin' Cranberry River at first light, one enormous hand reachin' for a moss-covered boulder. Hemlocks and rhododendrons crowd the banks. The creature's half-hid in mornin' fog, just clear enough you can't pretend it's a bear. Papaw said it turned and looked at him, calm as Sunday, then just walked on into the laurel."},
            {"slug": "sam-bigfoot-family", "title": "Family on the Allegheny Ridge", "medium": "Oils &amp; Gouache", "date": "Jun 18, 2002", "badge": "", "color": "#445533", "desc": "Three figures &mdash; a big'un, a middle-sized one, and a little'un &mdash; silhouetted on a rocky ridge at sundown, the Allegheny Mountains rollin' out blue behind 'em. Based on a report from a turkey hunter up near Durbin who said he watched a family of 'em for ten minutes 'fore they melted into the trees like smoke."},
            {"slug": "sam-pnw-nightwatch", "title": "Somethin' Outside the Tent", "medium": "Oils", "date": "May 5, 2002", "badge": "", "color": "#2a3322", "desc": "Painted from the perspective of somebody lookin' out a tent flap at night up in the Dolly Sods Wilderness. Flashlight beam cuts through the dark and catches ferns and birch trunks and, Lord have mercy, just barely visible between two big spruces, a pair of eyes reflectin' back about eight feet off the ground. Your blood runs cold just lookin' at it."},
            {"slug": "sam-bigfoot-snow", "title": "Tracks on Spruce Knob", "medium": "Gouache", "date": "Mar 28, 2002", "badge": "", "color": "#889999", "desc": "A trail of enormous barefoot prints crossin' a fresh snowfield on Spruce Knob, the highest point in West Virginia. They lead toward the dark spruce treeline where fog's gatherin'. One print is shown up close in the foreground, clear as day, seventeen inches long. No creature visible &mdash; just the undeniable proof that somethin' big walked through here while folks were sleepin'."},
        ],
    },
    {
        "slug": "jersey-pine",
        "name": "Piney Combs",
        "location": "Hinton, West Virginia, USA",
        "member_since": "January 2001",
        "media": "Ink, Watercolour",
        "influences": "Old-timey naturalist books from the library, Audubon prints, my daddy's field notebooks, pressed flowers and specimen jars",
        "bio": "Folks call me Piney on account of I'm always out in the pines sketchin'. I illustrate the cryptid critters of Appalachia like they was real animals in a naturalist's field guide &mdash; 'cause I reckon that's what they are. Things we ain't catalogued yet, is all. I use ink and watercolour on paper I tea-stain myself to look old-timey. Every creature gets proper Latin names, anatomical notes, and habitat descriptions, just like Mr. Audubon done with his birds. My daddy kept notebooks of every strange thing he saw in forty years of workin' for the Forest Service, and I'm turnin' his notes into art.",
        "total_images": 16,
        "total_comments": 91,
        "gallery_created": "January 20, 2001",
        "last_updated": "July 8, 2002",
        "artworks": [
            {"slug": "pine-jersey-devil", "title": "Field Guide Plate: The Snallygaster", "medium": "Ink &amp; Watercolour", "date": "Jul 8, 2002", "badge": "UPDATED!", "color": "#887755", "desc": "A proper naturalist illustration of the Snallygaster, that half-bird half-reptile terror of the Appalachian hills. Drawn like an Audubon plate with multiple views &mdash; wings spread, head detail, talon close-up &mdash; and handwritten field notes in the margins about reported sightin's from the Shenandoah Valley. My daddy seen one fly over Route 60 in 1978. He drew it in his notebook and I worked from that."},
            {"slug": "pine-thunderbird-plate", "title": "Field Guide Plate: The Appalachian Thunderbird", "medium": "Ink &amp; Watercolour", "date": "Jun 15, 2002", "badge": "", "color": "#998866", "desc": "A gorgeous naturalist plate of the great Thunderbird, wingspan marked at twenty-two feet, soarin' over the New River Gorge. Below I done a size comparison with a turkey vulture and a person standin' on the bridge. Annotated with altitude estimates and Cherokee names. The paper's stained with walnut ink to look like it come from an old book."},
            {"slug": "pine-champ-specimen", "title": "Field Guide Plate: The Greenbrier River Serpent", "medium": "Ink &amp; Watercolour", "date": "May 22, 2002", "badge": "", "color": "#667788", "desc": "Ain't many folks know about the Greenbrier River Serpent, but there's been sightin's goin' back to the 1800s. I drew it up proper: a long-necked critter about twenty feet, cross-section views of the neck, flipper detail, and hypothesized diet based on the river's fish population. Scientific as I could make it, which is pretty dang scientific if I say so myself."},
            {"slug": "pine-dover-demon", "title": "Field Guide Plate: The Grafton Monster", "medium": "Ink", "date": "Apr 3, 2002", "badge": "", "color": "#aabb99", "desc": "Pure ink study of the Grafton Monster, that headless, white-skinned thing spotted near Grafton, West Virginia in 1964. I drew it clinical-like, with measurements and witness descriptions around the border. The lack of a visible head is the most disturbin' part &mdash; where its face ought to be there's just smooth, pale skin like a boiled egg. Lord almighty."},
        ],
    },
    {
        "slug": "loch-lorna",
        "name": "Lorna Deepwater",
        "location": "Burnsville, North Carolina, USA",
        "member_since": "September 1999",
        "media": "Watercolour, Gouache",
        "influences": "Mountain lake reflections, Cherokee water spirit legends, foggy mornin's on the reservoir, my great-aunt Hazel's stories",
        "bio": "I paint the things that live in the deep, dark waters of these mountains. Now honey, folks think you gotta go to Scotland for lake monsters, but we got our own right here in Appalachia. The Altamaha-ha down in Georgia, the Chessie in the Chesapeake, whatever's makin' them strange waves on Fontana Lake at night. My great-aunt Hazel, God rest her, she lived on the shore of Watauga Lake her whole life and she said the TVA flooded more than just towns when they built them dams &mdash; they trapped somethin' down there that was old when the Cherokee was young. I paint what she described.",
        "total_images": 13,
        "total_comments": 72,
        "gallery_created": "September 3, 1999",
        "last_updated": "July 5, 2002",
        "artworks": [
            {"slug": "lorna-nessie-deep", "title": "What the Dam Drowned", "medium": "Watercolour &amp; Gouache", "date": "Jul 5, 2002", "badge": "UPDATED!", "color": "#2a4455", "desc": "An underwater view of somethin' ancient glidin' through the dark green water of Watauga Lake, passin' over the drowned ruins of old Butler, Tennessee. Shafts of mountain sunlight filter down from the surface, just barely lightin' up a long neck and a body that ain't no catfish. You can see the steeple of the old church below, and the creature's swimmin' right over it like it owns the place. 'Cause it does."},
            {"slug": "lorna-ogopogo", "title": "The Fontana Lake Thing", "medium": "Watercolour", "date": "Jun 12, 2002", "badge": "", "color": "#445566", "desc": "Three humps breakin' the surface of Fontana Lake at dusk, ringed by the Great Smoky Mountains. The water's glass-still 'cept where this critter's movin' through it, leavin' a wake that rocks every fishin' boat for a quarter mile. My aunt Hazel said on quiet nights you could hear it hummin' under the water, low and sad, like it remembered when the valley was dry."},
            {"slug": "lorna-kraken", "title": "The White Thing of the New River", "medium": "Gouache", "date": "May 1, 2002", "badge": "", "color": "#334455", "desc": "Now this one's based on stories from along the New River &mdash; oldest river in the Western Hemisphere, they say. Folks have reported a massive white shape movin' under the water near the old ferry crossin's for two hundred years. I painted it risin' up under a flatboat in the 1800s, a pale tentacled thing that could grab a horse off the bank. The boatmen are frozen in terror. Some say it's still down there, in the deep pools where the current slows."},
        ],
    },
    {
        "slug": "chupacabra-charlie",
        "name": "Charlie Ridgerunner",
        "location": "Wytheville, Virginia, USA",
        "member_since": "June 2001",
        "media": "Acrylic, Spray Paint, Digital",
        "influences": "Old barn signs, hand-painted road warnings, revival tent posters, my cousin Deke's trail camera photos",
        "bio": "Howdy, I'm Charlie and I paint cryptids the way they'd look on the side of a barn or a revival tent poster &mdash; big, bold, and scary as all get-out. I grew up in Wytheville, Virginia, which had them famous UFO sightin's back in the '80s, so strange is just part of the landscape 'round here. My cousin Deke's got trail cameras all over the mountain and every few months he gets somethin' on there that ain't no deer, ain't no bear, and ain't no person. I paint what Deke catches. Bold outlines, bright colours, the kind of thing that'd make you stomp the brakes if you saw it on a barn by the highway.",
        "total_images": 10,
        "total_comments": 63,
        "gallery_created": "June 6, 2001",
        "last_updated": "July 12, 2002",
        "artworks": [
            {"slug": "charlie-chupacabra-hunt", "title": "Somethin' Got the Goats", "medium": "Acrylic &amp; Spray Paint", "date": "Jul 12, 2002", "badge": "NEW!", "color": "#883322", "desc": "Now we ain't supposed to have Chupacabras in Virginia, but tell that to my Uncle Earl's goats. This paintin' shows what I reckon got 'em: a spiny, dog-like critter with eyes that glow green as antifreeze, crouchin' on a split-rail fence under a full moon. Painted barn-sign style, big and flat with bold black outlines. Earl swears he saw it. Earl also swears he don't drink no more. Make of that what you will."},
            {"slug": "charlie-lechuza", "title": "The Wytheville Lights", "medium": "Acrylic", "date": "Jun 20, 2002", "badge": "", "color": "#332244", "desc": "Back in '87, folks in Wytheville saw lights in the sky for months on end. I painted what my mama described seein' from our front porch &mdash; a cluster of lights hoverin' over the ridge, silent as death, while the dogs howled theirselves hoarse. Done in flat acrylic like a old-time sign, with my mama's exact words written around the border: 'Lord God, Charlie, don't look at it, don't you dare look at it.'"},
            {"slug": "charlie-donkey-lady", "title": "The Sheepsquatch", "medium": "Spray Paint &amp; Acrylic", "date": "May 8, 2002", "badge": "", "color": "#554422", "desc": "Y'all ever heard of the Sheepsquatch? White as snow, big as a pickup truck, with ram horns and a scream that'll peel paint off a barn. Spotted all over the TNT Area in Mason County and up through the Appalachian hills. I painted this one chargin' out of a laurel thicket at night, caught in truck headlights on a back road. The driver's about two seconds from discoverin' religion. Painted revival-poster style 'cause this critter is a come-to-Jesus moment on four legs."},
        ],
    },
    {
        "slug": "skunkape-shelly",
        "name": "Shelly Hogtooth",
        "location": "Elkview, West Virginia, USA",
        "member_since": "November 2001",
        "media": "Coloured Pencil, Digital",
        "influences": "Appalachian folk art, quiltin' patterns, old tintypes, my granny's cast iron cookware (for some reason)",
        "bio": "I'm Shelly and I draw the critters that folks in the hills have been seein' and not talkin' about for generations. Not just the famous ones like Mothman &mdash; the little weird ones too. The things your great-uncle saw by the crick that one time but won't discuss at Thanksgivin'. I draw 'em in coloured pencil, real detailed and careful, 'cause I think these critters deserve to be documented with respect. I work at the Kanawha County Library by day, and most of my reference material comes from local history collections that'd curl your hair. Elfwood's the only place people don't look at me funny when I talk about this stuff.",
        "total_images": 8,
        "total_comments": 42,
        "gallery_created": "November 15, 2001",
        "last_updated": "July 2, 2002",
        "artworks": [
            {"slug": "shelly-skunkape", "title": "The Vegetable Man of Kelly's Creek", "medium": "Coloured Pencil &amp; Digital", "date": "Jul 2, 2002", "badge": "", "color": "#445533", "desc": "Now this one's from my own county. Folks along Kelly's Creek been reportin' a tall, thin figure covered in what looks like moss or leaves, standin' stock-still in the tree line at dusk. Don't move, don't speak, just stands there smellin' like rotten cabbage. I drew it real careful from three different eyewitness descriptions, and bless their hearts, they all matched up. The detail in the moss-fur took me two whole weeks."},
            {"slug": "shelly-lizardman", "title": "The Hellhound of the Coal Camps", "medium": "Coloured Pencil", "date": "Jun 10, 2002", "badge": "", "color": "#336633", "desc": "In the old coal camp towns, miners told stories of a dog-like thing that glowed faint blue in the dark mine tunnels. Not a ghost, not a regular dog &mdash; somethin' in between. Eyes like hot coals, no sound when it walked, and it only appeared before a cave-in. Some said it was a warnin'. Some said it was the cause. I drew it in a tunnel mouth with a miner's lamp behind it, its shadow stretchin' long and wrong-shaped down the shaft."},
            {"slug": "shelly-altamaha", "title": "The Tailypo", "medium": "Digital &amp; Coloured Pencil", "date": "May 1, 2002", "badge": "", "color": "#556644", "desc": "Every child in Appalachia knows the Tailypo &mdash; the critter that comes scratchin' at your cabin door whisperin' 'Tailypo, tailypo, give me back my tailypo.' But ain't nobody drawn what it actually looks like. Based on the oldest tellin's I could find in the library archives, I drew it small and wiry, with hands like a raccoon and eyes like a person, creepin' along a cabin porch in the dead of night. The scratches on the door are already there."},
        ],
    },
]

def main():
    print("Generating cryptid artist pages...")
    file_count = 0

    for artist in CRYPTID_ARTISTS:
        slug = artist["slug"]

        # Generate profile SVG
        profile_svg = generate_profile_svg(slug)
        with open(os.path.join(IMG_DIR, f"{slug}-profile.svg"), "w") as f:
            f.write(profile_svg)
        file_count += 1

        # Generate artist page
        artist_page = generate_artist_page(artist)
        with open(os.path.join(BASE_DIR, f"{slug}.html"), "w") as f:
            f.write(artist_page)
        file_count += 1

        # Generate artwork SVGs and pages
        for i, artwork in enumerate(artist.get("artworks", [])):
            full_svg = generate_creature_svg(artwork)
            with open(os.path.join(IMG_DIR, f"{artwork['slug']}.svg"), "w") as f:
                f.write(full_svg)
            file_count += 1

            thumb_svg = generate_thumbnail_svg(artwork)
            with open(os.path.join(IMG_DIR, f"{artwork['slug']}-thumb.svg"), "w") as f:
                f.write(thumb_svg)
            file_count += 1

            artwork_page = generate_artwork_page(artist, artwork, i)
            with open(os.path.join(BASE_DIR, f"{artwork['slug']}.html"), "w") as f:
                f.write(artwork_page)
            file_count += 1

    print(f"Generated {file_count} files for {len(CRYPTID_ARTISTS)} cryptid artists!")

if __name__ == "__main__":
    main()
