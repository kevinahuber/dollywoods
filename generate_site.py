#!/usr/bin/env python3
"""Generate all artist pages, artwork pages, and SVG images for DOLLYWOODS."""

import os
import random
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "images")

os.makedirs(IMG_DIR, exist_ok=True)

# ============================================================
# DATA
# ============================================================

LOTHLORIEN_ARTISTS = [
    {
        "slug": "dolly-diamondfire",
        "name": "Dolly Diamondfire",
        "location": "Sevierville, Tennessee, USA",
        "member_since": "January 1997",
        "media": "Rhinestone-encrusted Watercolour, Glitter Digital (Photoshop 6.0 with extra sparkle)",
        "influences": "The Smoky Mountains, butterflies, my mama's quilt patterns, and a whole lotta love",
        "bio": "Well hey there, darlin'! Welcome to my little corner of Elfwood! I've been drawin' fantasy critters and sparkly things since I was knee-high to a grasshopper back in the hollers of Tennessee. I mostly paint butterflies with rhinestones, dragons in big wigs, and enchanted Smoky Mountain landscapes. Comments and sweet talk are always welcome!",
        "total_images": 27,
        "total_comments": 143,
        "gallery_created": "January 19, 1997",
        "last_updated": "July 12, 2002",
        "artworks": [
            {"slug": "rhinestone-dragon", "title": "Rhinestone Dragon at Sunset", "medium": "Watercolour &amp; Glitter", "date": "Jul 12, 2002", "badge": "NEW!", "color": "#cc88cc", "desc": "A magnificent purple dragon covered in rhinestones, perched on a cliff above Dollywood, wearin' a big blonde wig and spreadin' her bedazzled wings against a pink and gold Tennessee sunset."},
            {"slug": "butterfly-queen", "title": "The Butterfly Queen of Tennessee", "medium": "Watercolour", "date": "Jun 28, 2002", "badge": "", "color": "#ffccdd", "desc": "A regal queen adorned with butterfly wings made of pure Tennessee wildflower colours, sittin' on a throne of dogwood blossoms with monarch butterflies all around her crown."},
            {"slug": "9to5-sorceress", "title": "Workin' 9 to 5 (as a Sorceress)", "medium": "Pencil &amp; Digital", "date": "Jun 15, 2002", "badge": "", "color": "#ffdd88", "desc": "A sorceress in a sharp dragon-scale pantsuit carryin' a briefcase full of potions, headin' to her 9-to-5 job at the Enchantment Corporation. She's got a coffee in one hand and a wand in the other."},
            {"slug": "smoky-faeries", "title": "Faeries of the Smoky Mountains", "medium": "Digital (Photoshop)", "date": "May 30, 2002", "badge": "", "color": "#88ccaa", "desc": "A misty scene of tiny faeries dancin' through the morning fog of the Great Smoky Mountains, their wings catchin' the first light of dawn like little sparklers at a Fourth of July celebration."},
            {"slug": "jolene-elf-witch", "title": "Jolene the Elf Witch", "medium": "Watercolour", "date": "May 12, 2002", "badge": "", "color": "#eebb44", "desc": "An elf witch with auburn hair and emerald eyes, castin' a spell that looks suspiciously like she's stealin' someone's man. She's wearin' a green velvet gown with gold embroidery."},
            {"slug": "coat-many-colours", "title": "Coat of Many Colours (Magic Cloak)", "medium": "Acrylic &amp; Glitter", "date": "Apr 22, 2002", "badge": "", "color": "#ff9999", "desc": "A magic cloak made from scraps of enchanted fabric, each patch containin' a different spell. Inspired by my mama's quilt and the song that makes me cry every dang time."},
            {"slug": "unicorn-big-wig", "title": "Unicorn in a Big Wig", "medium": "Watercolour &amp; Ink", "date": "Apr 5, 2002", "badge": "", "color": "#ddaaff", "desc": "A majestic unicorn wearin' the biggest, most fabulous blonde wig you ever did see. Her horn is bedazzled with rhinestones and her mane is teased to the heavens."},
            {"slug": "enchanted-castle", "title": "The Enchanted Castle of Dollywood", "medium": "Pencil &amp; Rhinestones", "date": "Mar 18, 2002", "badge": "", "color": "#aaddcc", "desc": "A fantasy castle inspired by Dollywood, with rhinestone-studded turrets, butterfly flags, and a rainbow bridge leadin' to the front gate. It's the happiest place in any realm!"},
        ],
    },
    {
        "slug": "arwen-starweaver",
        "name": "Arwen Starweaver",
        "location": "Portland, Oregon, USA",
        "member_since": "March 1999",
        "media": "Pencil, Watercolour",
        "influences": "Pre-Raphaelite art, Brian Froud, Celtic mythology",
        "bio": "Hello there! I'm a self-taught artist who fell in love with fantasy art after reading The Lord of the Rings at age twelve. I specialize in ethereal portraits of elves and forest spirits, always trying to capture that magical twilight feeling. Currently studying art history at Portland State.",
        "total_images": 12,
        "total_comments": 67,
        "gallery_created": "March 14, 1999",
        "last_updated": "June 30, 2002",
        "artworks": [
            {"slug": "starweaver-moonlit-elf", "title": "Moonlit Elf Portrait", "medium": "Pencil &amp; Watercolour", "date": "Jun 30, 2002", "badge": "", "color": "#8899cc", "desc": "A delicate elf maiden with silver hair gazing at the full moon, her eyes reflecting starlight. Drawn in soft pencil with watercolour washes for the midnight blue background."},
            {"slug": "starweaver-forest-spirit", "title": "Spirit of the Ancient Oak", "medium": "Watercolour", "date": "Jun 12, 2002", "badge": "", "color": "#669966", "desc": "A tree spirit emerging from the bark of a thousand-year-old oak, her form half wood and half ethereal light, with leaves for hair and acorns for jewellery."},
            {"slug": "starweaver-celtic-dragon", "title": "Celtic Knotwork Dragon", "medium": "Pencil &amp; Ink", "date": "May 20, 2002", "badge": "", "color": "#996633", "desc": "An intricate dragon rendered entirely in Celtic knotwork patterns, its body weaving in and out of an illuminated manuscript border."},
        ],
    },
    {
        "slug": "aldric-wanderer",
        "name": "Aldric the Wanderer",
        "location": "Munich, Germany",
        "member_since": "November 2001",
        "media": "Digital, Ink",
        "influences": "Tolkien, Warhammer Fantasy, medieval European art",
        "bio": "Greetings, fellow travellers! I am a concept artist by day and a fantasy world-builder by night. My art focuses on dark fantasy landscapes and armoured warriors. I draw inspiration from medieval European history and the wild forests of Bavaria. New to Elfwood but already feeling at home!",
        "total_images": 8,
        "total_comments": 34,
        "gallery_created": "November 3, 2001",
        "last_updated": "July 2, 2002",
        "artworks": [
            {"slug": "aldric-dark-knight", "title": "The Dark Knight of Bavaria", "medium": "Digital &amp; Ink", "date": "Jul 2, 2002", "badge": "NEW!", "color": "#445566", "desc": "A heavily armoured knight standing in a moonlit Bavarian forest, his enchanted sword glowing with pale blue runes. The trees around him are gnarled and ancient."},
            {"slug": "aldric-fortress", "title": "Fortress of the Mountain King", "medium": "Digital", "date": "Jun 15, 2002", "badge": "", "color": "#667788", "desc": "A massive dwarven fortress carved into the face of a snow-capped mountain, with bridges spanning deep chasms and forge-fire glowing from every window."},
            {"slug": "aldric-wyvern", "title": "Wyvern at Dawn", "medium": "Ink &amp; Digital Colour", "date": "May 28, 2002", "badge": "", "color": "#887766", "desc": "A wyvern perched on a ruined tower at dawn, silhouetted against a blood-red sky. Its wings are tattered but magnificent."},
        ],
    },
    {
        "slug": "astrid-fjordmist",
        "name": "Astrid Fjordmist",
        "location": "Bergen, Norway",
        "member_since": "June 1998",
        "media": "Oils, Acrylic",
        "influences": "Norse mythology, fjord landscapes, Scandinavian folk art",
        "bio": "Hei! I paint creatures from Norse mythology set against the dramatic landscapes of my homeland. My studio overlooks a fjord, and the changing light inspires everything I create. I work primarily in oils and acrylics on large canvases, which I then photograph and scan for Elfwood.",
        "total_images": 23,
        "total_comments": 112,
        "gallery_created": "June 22, 1998",
        "last_updated": "May 17, 2002",
        "artworks": [
            {"slug": "astrid-frost-giant", "title": "Frost Giant of the North", "medium": "Oils", "date": "May 17, 2002", "badge": "", "color": "#aabbdd", "desc": "A colossal frost giant emerging from a glacial fjord, ice crystals forming in his breath. The aurora borealis dances across the sky behind him."},
            {"slug": "astrid-valkyrie", "title": "Valkyrie's Ride", "medium": "Acrylic", "date": "Apr 30, 2002", "badge": "", "color": "#ccaa88", "desc": "A valkyrie riding a winged horse through storm clouds, her golden armour blazing with divine light as she descends to choose the worthy fallen."},
            {"slug": "astrid-sea-serpent", "title": "Jormungandr Rising", "medium": "Oils &amp; Gold Leaf", "date": "Mar 8, 2002", "badge": "", "color": "#5588aa", "desc": "The great world serpent Jormungandr rising from the depths of a Norwegian fjord, sending massive waves crashing against the rocky shores."},
        ],
    },
    {
        "slug": "bramblewood",
        "name": "Bramblewood",
        "location": "Somerset, England, UK",
        "member_since": "February 2002",
        "media": "Pencil",
        "influences": "Arthur Rackham, Beatrix Potter, English countryside",
        "bio": "Hello! I'm Bramblewood (not my real name, obviously). I draw little woodland creatures in pencil - hedgehogs in armour, mice with swords, that sort of thing. Inspired by the fields and forests near my home in Somerset. Everything is done in graphite pencil on cartridge paper.",
        "total_images": 6,
        "total_comments": 28,
        "gallery_created": "February 8, 2002",
        "last_updated": "July 10, 2002",
        "artworks": [
            {"slug": "bramble-hedgehog-knight", "title": "Sir Prickles the Brave", "medium": "Pencil", "date": "Jul 10, 2002", "badge": "NEW!", "color": "#aa9977", "desc": "A hedgehog knight in tiny plate armour, wielding a thorn sword and carrying a leaf shield, standing guard at the entrance to a mushroom village."},
            {"slug": "bramble-mouse-wizard", "title": "The Mouse Wizard's Tower", "medium": "Pencil", "date": "Jun 22, 2002", "badge": "", "color": "#bbaa88", "desc": "A field mouse in wizard robes standing atop a stack of old books that serves as his tower, casting a spell that makes dandelion seeds float in spirals."},
        ],
    },
    {
        "slug": "brynn-ashfallow",
        "name": "Brynn Ashfallow",
        "location": "Vancouver, BC, Canada",
        "member_since": "September 1999",
        "media": "Watercolour, Coloured Pencil",
        "influences": "Yoshitaka Amano, Art Nouveau, Pacific Northwest nature",
        "bio": "Hi! I'm a graphic design student who spends way too much time painting fantasy creatures instead of doing my homework. My style mixes Art Nouveau elegance with Japanese illustration influences. I love painting dragons, phoenixes, and anything with elaborate wings or flowing hair.",
        "total_images": 15,
        "total_comments": 89,
        "gallery_created": "September 19, 1999",
        "last_updated": "April 23, 2002",
        "artworks": [
            {"slug": "brynn-phoenix-rising", "title": "Phoenix Rising", "medium": "Watercolour", "date": "Apr 23, 2002", "badge": "", "color": "#ff8844", "desc": "A phoenix bursting from flames in an explosion of gold and crimson, its tail feathers flowing in Art Nouveau curves against a deep navy sky."},
            {"slug": "brynn-water-dragon", "title": "Dragon of the Pacific", "medium": "Watercolour &amp; Coloured Pencil", "date": "Mar 15, 2002", "badge": "", "color": "#44aacc", "desc": "A serpentine water dragon coiling through Pacific Northwest waves, its scales shimmering blue-green like abalone shells, with misty rainforest visible on the shore."},
            {"slug": "brynn-moth-fairy", "title": "The Moth Fairy", "medium": "Coloured Pencil", "date": "Feb 1, 2002", "badge": "", "color": "#cc99bb", "desc": "A delicate fairy with luna moth wings, drawn entirely in coloured pencil with incredible detail in the wing patterns. She sits on a moonflower."},
        ],
    },
    {
        "slug": "celeste-ravenmark",
        "name": "Celeste Ravenmark",
        "location": "New York City, NY, USA",
        "member_since": "August 1997",
        "media": "Digital, Photoshop",
        "influences": "Luis Royo, Brom, gothic architecture",
        "bio": "Dark fantasy is my domain. I create digital paintings of gothic castles, shadow creatures, and warriors who dwell in the spaces between light and dark. I've been on Elfwood since nearly the beginning and I've watched this community grow into something magical. NYC provides endless inspiration for dark, moody atmospheres.",
        "total_images": 31,
        "total_comments": 156,
        "gallery_created": "August 2, 1997",
        "last_updated": "July 14, 2002",
        "artworks": [
            {"slug": "celeste-shadow-dragon", "title": "Shadow Dragon's Lair", "medium": "Digital (Photoshop)", "date": "Jul 14, 2002", "badge": "UPDATED!", "color": "#443355", "desc": "A dragon made of living shadow curled around a hoard of dark crystals in a gothic cathedral, only its glowing purple eyes visible in the darkness."},
            {"slug": "celeste-dark-sorceress", "title": "The Raven Queen", "medium": "Digital (Photoshop)", "date": "Jun 20, 2002", "badge": "", "color": "#332244", "desc": "A dark sorceress standing on a tower balcony with ravens swirling around her, her cloak made of shadow and starlight, overlooking a city of gothic spires."},
            {"slug": "celeste-gargoyle", "title": "Gargoyle Awakening", "medium": "Digital", "date": "May 5, 2002", "badge": "", "color": "#556655", "desc": "A stone gargoyle cracking free from its perch on a cathedral, stone fragments falling as living flesh is revealed beneath, wings unfurling against a stormy sky."},
        ],
    },
    {
        "slug": "corvin-nighthollow",
        "name": "Corvin Nighthollow",
        "location": "Edinburgh, Scotland, UK",
        "member_since": "January 2001",
        "media": "Ink, Digital",
        "influences": "Mike Mignola, medieval bestiaries, Scottish folklore",
        "bio": "I draw monsters. Lots and lots of monsters. My style is heavy on black ink with minimal colour - think medieval bestiary meets comic book art. I'm particularly fond of creatures from Scottish and Irish folklore. Based in Edinburgh, surrounded by enough history and spookiness to last a lifetime.",
        "total_images": 9,
        "total_comments": 41,
        "gallery_created": "January 15, 2001",
        "last_updated": "June 5, 2002",
        "artworks": [
            {"slug": "corvin-kelpie", "title": "The Kelpie of Loch Morar", "medium": "Ink", "date": "Jun 5, 2002", "badge": "", "color": "#334455", "desc": "A kelpie emerging from a dark Scottish loch, half horse and half water creature, rendered in stark black and white ink with incredible cross-hatching detail."},
            {"slug": "corvin-redcap", "title": "Redcap", "medium": "Ink &amp; Digital Colour", "date": "May 1, 2002", "badge": "", "color": "#553333", "desc": "A terrifying Redcap goblin lurking in the ruins of a Scottish border castle, its iron boots and pike rendered in heavy black ink with splashes of crimson."},
        ],
    },
    {
        "slug": "duskrender",
        "name": "Duskrender",
        "location": "Austin, Texas, USA",
        "member_since": "April 2000",
        "media": "Acrylic, Gouache",
        "influences": "Frank Frazetta, Boris Vallejo, Southwestern landscapes",
        "bio": "Howdy! I paint traditional fantasy scenes with a Southwestern twist - think dragons in desert canyons, wizards under big Texas skies, and mythical creatures adapted to arid landscapes. I work almost exclusively in acrylic and gouache because I like how fast they dry in the Texas heat.",
        "total_images": 18,
        "total_comments": 95,
        "gallery_created": "April 11, 2000",
        "last_updated": "June 22, 2002",
        "artworks": [
            {"slug": "dusk-desert-dragon", "title": "Canyon Dragon", "medium": "Acrylic", "date": "Jun 22, 2002", "badge": "", "color": "#cc8844", "desc": "A massive red dragon nesting in a desert canyon at sunset, the sandstone walls glowing orange and the dragon's scales matching perfectly with the landscape."},
            {"slug": "dusk-thunderbird", "title": "Thunderbird Over Texas", "medium": "Acrylic &amp; Gouache", "date": "May 15, 2002", "badge": "", "color": "#8877aa", "desc": "A great thunderbird with lightning crackling from its wings, soaring over the Texas Hill Country during a dramatic summer thunderstorm."},
            {"slug": "dusk-cactus-elemental", "title": "Cactus Elemental", "medium": "Gouache", "date": "Apr 3, 2002", "badge": "", "color": "#77aa66", "desc": "A towering elemental made of living saguaro cacti, with flowers blooming from its joints and tiny desert creatures sheltering in its crevices."},
        ],
    },
    {
        "slug": "elara-moonshadow",
        "name": "Elara Moonshadow",
        "location": "Dublin, Ireland",
        "member_since": "October 1997",
        "media": "Watercolour, Digital",
        "influences": "Alan Lee, John Howe, Irish landscape painting",
        "bio": "I've been painting fantasy scenes since before the Internet was a thing, and Elfwood has been my artistic home since 1997. My work blends traditional watercolour with digital finishing touches. I'm drawn to misty landscapes, ancient ruins, and the feeling of magic lurking just beyond sight in the Irish countryside.",
        "total_images": 27,
        "total_comments": 134,
        "gallery_created": "October 8, 1997",
        "last_updated": "July 12, 2002",
        "artworks": [
            {"slug": "elara-fairy-ring", "title": "The Fairy Ring at Dawn", "medium": "Watercolour &amp; Digital", "date": "Jul 12, 2002", "badge": "UPDATED!", "color": "#99bb88", "desc": "A circle of ancient standing stones surrounded by glowing mushrooms, tiny faeries dancing in the mist at the first light of dawn over the Irish countryside."},
            {"slug": "elara-selkie", "title": "The Selkie's Return", "medium": "Watercolour", "date": "Jun 18, 2002", "badge": "", "color": "#6699aa", "desc": "A selkie woman shedding her seal skin on a rocky Irish shore, the ocean behind her churning with moonlight and mystery."},
            {"slug": "elara-green-dragon", "title": "Dragon of the Emerald Isle", "medium": "Watercolour &amp; Digital", "date": "May 2, 2002", "badge": "", "color": "#448855", "desc": "A gentle green dragon curled around a ruined Irish round tower, moss growing on its scales, watching over a misty valley with ancient wisdom in its eyes."},
        ],
    },
    {
        "slug": "ember-ashgrove",
        "name": "Ember Ashgrove",
        "location": "Asheville, NC, USA",
        "member_since": "May 2002",
        "media": "Pencil, Charcoal",
        "influences": "Brian Froud, Jim Henson, Appalachian folklore",
        "bio": "Brand new to Elfwood! I just started sharing my art online and I'm so nervous! I draw fantasy creatures inspired by Appalachian folklore - think Jack Tales meets fairy tales. Everything is pencil and charcoal because I can't afford fancy art supplies yet (college student life!). Feedback welcome, please be gentle!",
        "total_images": 5,
        "total_comments": 19,
        "gallery_created": "May 3, 2002",
        "last_updated": "July 1, 2002",
        "artworks": [
            {"slug": "ember-jack-tales", "title": "Jack and the Beanstalk Giant", "medium": "Charcoal", "date": "Jul 1, 2002", "badge": "", "color": "#777766", "desc": "A dramatic charcoal drawing of the giant from Jack and the Beanstalk, reimagined as an Appalachian mountain spirit, towering over misty hollers and tiny cabins."},
            {"slug": "ember-deer-woman", "title": "The Deer Woman", "medium": "Pencil", "date": "Jun 10, 2002", "badge": "", "color": "#998877", "desc": "A haunting pencil sketch of the Deer Woman from Cherokee legend, half woman and half white-tailed deer, standing in a moonlit clearing in the Appalachian woods."},
        ],
    },
    {
        "slug": "firebrand-ferris",
        "name": "Firebrand Ferris",
        "location": "Melbourne, Australia",
        "member_since": "July 2000",
        "media": "Digital, 3D Render",
        "influences": "H.R. Giger, Syd Mead, Australian outback",
        "bio": "G'day! I create fantasy and sci-fi crossover art using a mix of 2D digital painting and 3D renders in Bryce and Poser. I love blending organic fantasy creatures with mechanical elements. When I'm not making art, I'm studying computer science at uni. The Australian outback is surprisingly inspiring for alien landscapes!",
        "total_images": 11,
        "total_comments": 52,
        "gallery_created": "July 19, 2000",
        "last_updated": "May 30, 2002",
        "artworks": [
            {"slug": "ferris-mech-dragon", "title": "Mechanical Dragon MK-VII", "medium": "3D Render &amp; Digital Paint", "date": "May 30, 2002", "badge": "", "color": "#887766", "desc": "A biomechanical dragon made of brass gears and living flesh, steam venting from its joints as it spreads copper-plated wings over a steampunk cityscape."},
            {"slug": "ferris-crystal-golem", "title": "Crystal Golem", "medium": "3D Render (Bryce)", "date": "Apr 18, 2002", "badge": "", "color": "#99aacc", "desc": "A golem made entirely of translucent crystal, light refracting through its body to cast rainbow patterns on the cave walls around it."},
            {"slug": "ferris-fire-elemental", "title": "Elemental Forge", "medium": "Digital", "date": "Mar 5, 2002", "badge": "", "color": "#cc6633", "desc": "A fire elemental working at a massive forge, its body a swirling mass of flame and molten metal, hammering a glowing sword on an anvil of obsidian."},
        ],
    },
]

ZONE47_ARTISTS = [
    {
        "slug": "axiom-9",
        "name": "Axiom-9",
        "location": "Tokyo, Japan",
        "member_since": "December 2001",
        "media": "Digital, 3D Render",
        "influences": "Masamune Shirow, Katsuhiro Otomo, cyberpunk aesthetics",
        "bio": "Hello! I am a CG artist creating science fiction illustrations inspired by cyberpunk anime and manga. I work primarily in Photoshop and 3ds Max. My focus is on mecha designs, cybernetic characters, and neon-lit cityscapes. Earth timezone: UTC+9.",
        "total_images": 14,
        "total_comments": 58,
        "gallery_created": "December 12, 2001",
        "last_updated": "July 8, 2002",
        "section": "zone47",
        "artworks": [
            {"slug": "axiom-neon-mecha", "title": "Neon Ronin MK-III", "medium": "3D Render &amp; Digital", "date": "Jul 8, 2002", "badge": "NEW!", "color": "#4455aa", "desc": "A sleek combat mecha standing in a neon-lit Tokyo alleyway, rain streaming down its polished armour, holographic advertisements reflected in its visor."},
            {"slug": "axiom-space-station", "title": "Orbital Station Prometheus", "medium": "3D Render", "date": "Jun 20, 2002", "badge": "", "color": "#223355", "desc": "A massive ring-shaped space station orbiting a gas giant, tiny ships docking at its ports while the planet's storms rage in the background."},
            {"slug": "axiom-cyborg", "title": "Chrome Angel", "medium": "Digital (Photoshop)", "date": "May 15, 2002", "badge": "", "color": "#556688", "desc": "A cybernetic woman with chrome angel wings and glowing circuitry beneath translucent skin, floating in a digital void of streaming data."},
        ],
    },
    {
        "slug": "binary-frost",
        "name": "Binary Frost",
        "location": "Stockholm, Sweden",
        "member_since": "March 2001",
        "media": "Digital, Photoshop",
        "influences": "Chris Foss, Peter Elson, classic sci-fi book covers",
        "bio": "I paint spaceships. Big ones, small ones, weird ones. If it flies through space, I want to paint it. My style is heavily influenced by the classic sci-fi book cover artists of the 70s and 80s. I work in Photoshop with a Wacom tablet and way too many custom brushes.",
        "total_images": 7,
        "total_comments": 31,
        "gallery_created": "March 5, 2001",
        "last_updated": "June 19, 2002",
        "section": "zone47",
        "artworks": [
            {"slug": "binary-generation-ship", "title": "The Generation Ship Exodus", "medium": "Digital (Photoshop)", "date": "Jun 19, 2002", "badge": "", "color": "#334466", "desc": "A kilometres-long generation ship drifting through a nebula, its hull covered in centuries of micro-meteor impacts, a tiny blue sun reflecting off its solar sails."},
            {"slug": "binary-fighter", "title": "Interceptor Class VII", "medium": "Digital", "date": "May 8, 2002", "badge": "", "color": "#445577", "desc": "A sleek fighter craft banking through an asteroid field, engines blazing orange against the cold blue of deep space, narrowly avoiding tumbling rocks."},
        ],
    },
    {
        "slug": "cpt-jasper-voss",
        "name": "Cpt. Jasper Voss",
        "location": "Houston, Texas, USA",
        "member_since": "May 1998",
        "media": "Acrylic, Airbrush",
        "influences": "NASA concept art, Ralph McQuarrie, retro-futurism",
        "bio": "Retired Air Force, current space nut. I paint retro-futuristic scenes inspired by golden age sci-fi and NASA concept art. My studio is full of model rockets and vintage pulp magazines. I use traditional airbrush and acrylic because real artists don't need no stinkin' computer (just kidding, digital folks, y'all are great too).",
        "total_images": 19,
        "total_comments": 87,
        "gallery_created": "May 20, 1998",
        "last_updated": "July 5, 2002",
        "section": "zone47",
        "artworks": [
            {"slug": "voss-mars-colony", "title": "First Light on Mars Colony", "medium": "Acrylic &amp; Airbrush", "date": "Jul 5, 2002", "badge": "UPDATED!", "color": "#cc6644", "desc": "A retro-futuristic Mars colony at dawn, dome habitats glowing warm against the rusty landscape, an American flag planted beside the main airlock, and Earth visible as a blue dot in the pink sky."},
            {"slug": "voss-space-battle", "title": "Battle of Cygnus Station", "medium": "Acrylic", "date": "Jun 12, 2002", "badge": "", "color": "#443366", "desc": "A dramatic space battle between gleaming silver warships and alien craft, laser beams crisscrossing the void, explosions blooming silently against a backdrop of stars."},
            {"slug": "voss-alien-market", "title": "The Alien Bazaar", "medium": "Airbrush &amp; Acrylic", "date": "May 1, 2002", "badge": "", "color": "#886644", "desc": "A bustling alien marketplace on a desert planet, dozens of different species haggling over exotic goods under twin suns, rendered in warm retro-pulp colours."},
        ],
    },
    {
        "slug": "chromia-vex",
        "name": "Chromia Vex",
        "location": "Berlin, Germany",
        "member_since": "August 2000",
        "media": "Digital, Painter",
        "influences": "Moebius, Philippe Druillet, European comics",
        "bio": "Hallo! I create psychedelic science fiction art inspired by European comic traditions, especially French and Belgian bande dessinee. My work features alien landscapes, bizarre creatures, and surreal colour palettes. I use Corel Painter because it lets me get those organic brush textures I love.",
        "total_images": 11,
        "total_comments": 48,
        "gallery_created": "August 14, 2000",
        "last_updated": "June 28, 2002",
        "section": "zone47",
        "artworks": [
            {"slug": "chromia-alien-garden", "title": "The Chromatic Garden", "medium": "Digital (Painter)", "date": "Jun 28, 2002", "badge": "", "color": "#cc44aa", "desc": "A surreal alien garden with bioluminescent plants in impossible colours, fractal flowers that grow in mathematical spirals, and tiny insectoid creatures tending them."},
            {"slug": "chromia-nebula-whale", "title": "Nebula Whale", "medium": "Digital (Painter)", "date": "May 22, 2002", "badge": "", "color": "#6644aa", "desc": "A space whale the size of a moon drifting through a psychedelic nebula, smaller creatures swimming in its wake, its body covered in bioluminescent patterns."},
        ],
    },
    {
        "slug": "darkstar-mechworks",
        "name": "Darkstar Mechworks",
        "location": "Detroit, Michigan, USA",
        "member_since": "January 2000",
        "media": "Ink, Digital Colour",
        "influences": "Syd Mead, anime mecha, industrial design",
        "bio": "I design giant robots. That's it, that's the bio. Fine, a little more: I'm a mechanical engineering student who channels my love of giant stompy machines into detailed mecha illustrations. I start with ink on paper for the linework, then colour digitally. Detroit's industrial landscape is my muse.",
        "total_images": 22,
        "total_comments": 103,
        "gallery_created": "January 8, 2000",
        "last_updated": "July 11, 2002",
        "section": "zone47",
        "artworks": [
            {"slug": "darkstar-titan-mech", "title": "Titan-Class Heavy Assault Mech", "medium": "Ink &amp; Digital Colour", "date": "Jul 11, 2002", "badge": "", "color": "#556644", "desc": "A massive bipedal war machine bristling with weapons, standing in the ruins of a city. Every rivet, hatch, and armour plate is meticulously detailed in ink."},
            {"slug": "darkstar-dropship", "title": "Orbital Dropship Raven", "medium": "Ink &amp; Digital", "date": "Jun 5, 2002", "badge": "", "color": "#445555", "desc": "A military dropship descending through atmosphere, heat shields glowing red, with detailed cross-section showing the mecha stored in its cargo bay."},
            {"slug": "darkstar-repair-bay", "title": "Mech Repair Bay", "medium": "Ink", "date": "Apr 20, 2002", "badge": "", "color": "#666655", "desc": "A busy mech repair facility with mechanics swarming over a damaged giant robot, cranes and welding sparks everywhere. Pure ink linework, no colour."},
        ],
    },
    {
        "slug": "echo-nebula",
        "name": "Echo Nebula",
        "location": "San Francisco, CA, USA",
        "member_since": "November 1999",
        "media": "Mixed Media",
        "influences": "Afrofuturism, Sun Ra, Octavia Butler, cosmic art",
        "bio": "I create Afrofuturist science fiction art that imagines Black futures among the stars. My mixed media approach combines acrylic painting, collage, and digital elements. Inspired by Sun Ra, Octavia Butler, and the cosmic jazz tradition. San Francisco's diversity feeds my vision of inclusive futures.",
        "total_images": 16,
        "total_comments": 76,
        "gallery_created": "November 22, 1999",
        "last_updated": "May 14, 2002",
        "section": "zone47",
        "artworks": [
            {"slug": "echo-cosmic-queen", "title": "Cosmic Queen of the Diaspora", "medium": "Acrylic &amp; Collage", "date": "May 14, 2002", "badge": "", "color": "#774488", "desc": "A regal figure with an afro that contains galaxies, seated on a throne made of orbiting planets, her robes flowing like nebulae across the canvas."},
            {"slug": "echo-solar-ship", "title": "Solar Ark", "medium": "Mixed Media &amp; Digital", "date": "Apr 8, 2002", "badge": "", "color": "#cc8844", "desc": "A golden spacecraft shaped like an ancient Egyptian solar barque, sailing through space powered by captured starlight, crewed by figures in Afrofuturist attire."},
            {"slug": "echo-alien-jazz", "title": "Jazz on Jupiter", "medium": "Acrylic &amp; Collage", "date": "Feb 20, 2002", "badge": "", "color": "#885533", "desc": "Musicians playing cosmic jazz in a floating club in Jupiter's atmosphere, the Great Red Spot visible through panoramic windows, music notes transforming into stars."},
        ],
    },
    {
        "slug": "flux-capacitor",
        "name": "Flux Capacitor",
        "location": "Brisbane, Australia",
        "member_since": "June 2002",
        "media": "Digital, Bryce 3D",
        "influences": "Roger Dean, 70s prog rock album art, coral reefs",
        "bio": "Brand spanking new to Elfwood! I make alien landscapes in Bryce 3D and then paint over them in Photoshop. My style is heavily influenced by Roger Dean's Yes album covers - floating islands, impossible rock formations, alien skies. The Great Barrier Reef also inspires a lot of my organic alien world designs.",
        "total_images": 9,
        "total_comments": 22,
        "gallery_created": "June 1, 2002",
        "last_updated": "July 13, 2002",
        "section": "zone47",
        "artworks": [
            {"slug": "flux-floating-islands", "title": "Floating Islands of Kepler-442b", "medium": "Bryce 3D &amp; Photoshop", "date": "Jul 13, 2002", "badge": "NEW!", "color": "#44aa88", "desc": "Massive floating islands covered in alien coral and bioluminescent vegetation, connected by natural stone bridges, hovering above a turquoise ocean under twin suns."},
            {"slug": "flux-crystal-caves", "title": "The Crystal Caves of Proxima", "medium": "Bryce 3D", "date": "Jun 25, 2002", "badge": "", "color": "#88aacc", "desc": "An enormous underground cave system filled with house-sized crystals that glow with internal light, reflected in still underground pools, with alien explorers for scale."},
        ],
    },
]

WYVERNS_LIBRARY_AUTHORS = [
    {
        "slug": "arielle-thornscribe",
        "name": "Arielle Thornscribe",
        "location": "Boston, Massachusetts, USA",
        "member_since": "April 1999",
        "media": "Fiction &amp; Poetry",
        "influences": "Ursula K. Le Guin, Robin Hobb, medieval history",
        "bio": "I write stories about people in extraordinary circumstances making difficult choices. My current big project is 'The Last Dragon of Winterpeak,' a multi-chapter epic about the last surviving dragon and the young woman tasked with deciding its fate. I also write poetry when the mood strikes. English lit major, tea addict, cat person.",
        "total_images": 0,
        "total_comments": 82,
        "gallery_created": "April 14, 1999",
        "last_updated": "July 9, 2002",
        "is_writer": True,
        "stories": [
            {"slug": "arielle-last-dragon", "title": "The Last Dragon of Winterpeak", "genre": "High Fantasy", "words": "12,400", "status": "Chapters 1-5", "date": "Jul 9, 2002", "badge": "UPDATED!", "desc": "In the frozen peaks of Winterhold, the last living dragon slumbers beneath a glacier. When young scholar Maren discovers its hiding place, she must choose between her kingdom's safety and the survival of the world's last magical creature."},
            {"slug": "arielle-moonlit-crossroads", "title": "Moonlit Crossroads", "genre": "Dark Fantasy", "words": "3,200", "status": "Complete", "date": "May 20, 2002", "badge": "", "desc": "A traveller reaches a crossroads at midnight and meets three figures, each offering a different path. A meditation on choice, fate, and the roads not taken."},
            {"slug": "arielle-silver-court", "title": "Songs of the Silver Court", "genre": "Fantasy Poetry", "words": "800", "status": "Complete", "date": "Mar 8, 2002", "badge": "", "desc": "A cycle of five poems about the fey court of the Silver Queen, written in ballad metre. Explores themes of beauty, deception, and the price of immortality."},
        ],
    },
    {
        "slug": "basalt-greymantle",
        "name": "Basalt Greymantle",
        "location": "Birmingham, England, UK",
        "member_since": "October 2001",
        "media": "Epic Fantasy Fiction",
        "influences": "Tolkien, David Gemmell, military history",
        "bio": "I write epic fantasy with a focus on dwarves, because someone has to give the short folk their due! My ongoing series 'The Dwarven Chronicles' follows a clan of dwarven warriors through a war that will determine the fate of the underground kingdoms. I'm a history teacher by day, fantasy author by night.",
        "total_images": 0,
        "total_comments": 45,
        "gallery_created": "October 22, 2001",
        "last_updated": "June 15, 2002",
        "is_writer": True,
        "stories": [
            {"slug": "basalt-iron-stone", "title": "The Dwarven Chronicles: Iron and Stone", "genre": "Epic Fantasy", "words": "28,600", "status": "Chapters 1-9 (In Progress)", "date": "Jun 15, 2002", "badge": "", "desc": "When the great forge-city of Khazadbar is besieged by an army of trolls, grizzled veteran Thorin Ironhand must lead a desperate counter-attack through the ancient tunnels beneath the mountain."},
        ],
    },
    {
        "slug": "cassia-nightbloom",
        "name": "Cassia Nightbloom",
        "location": "Montreal, Quebec, Canada",
        "member_since": "January 2002",
        "media": "Science Fiction &amp; Fantasy Fiction",
        "influences": "Ursula K. Le Guin, Philip K. Dick, Margaret Atwood",
        "bio": "Bonjour! I write stories that blur the line between science fiction and fantasy. What if magic was just technology we don't understand yet? What if the future looks more like the past than we expect? I explore these questions through short stories and novellas. New to Elfwood and absolutely loving this community!",
        "total_images": 0,
        "total_comments": 56,
        "gallery_created": "January 8, 2002",
        "last_updated": "July 14, 2002",
        "is_writer": True,
        "stories": [
            {"slug": "cassia-echoes-nebula", "title": "Echoes from the Nebula", "genre": "Science Fiction", "words": "8,100", "status": "Complete", "date": "Jul 14, 2002", "badge": "", "desc": "An astronomer receives a signal from a dying nebula that contains what appears to be a voice speaking an ancient language. As she decodes it, she realizes it's a warning."},
            {"slug": "cassia-mechanic-familiar", "title": "The Mechanic's Familiar", "genre": "Steampunk", "words": "5,300", "status": "Complete", "date": "Jun 2, 2002", "badge": "", "desc": "In a steampunk city where magic and machines coexist, a mechanic discovers that the clockwork cat she built has developed a soul."},
            {"slug": "cassia-stardust-sorcery", "title": "Stardust and Sorcery", "genre": "Science Fantasy", "words": "15,200", "status": "Chapters 1-4 (In Progress)", "date": "Jul 14, 2002", "badge": "NEW!", "desc": "On a planet where starlight grants magical powers, a young astronomer must navigate a world of sorcerer-scientists to uncover why the stars are going dark."},
            {"slug": "cassia-three-wishes", "title": "Three Wishes (And a Dragon)", "genre": "Humorous Fantasy", "words": "2,100", "status": "Complete", "date": "Apr 1, 2002", "badge": "", "desc": "A dragon grants a peasant three wishes. The peasant uses them all on increasingly ridiculous requests. The dragon is not amused. Comedy ensues."},
        ],
    },
    {
        "slug": "drakon-quillsworth",
        "name": "Drakon Quillsworth",
        "location": "London, England, UK",
        "member_since": "August 2000",
        "media": "Hard Science Fiction",
        "influences": "Arthur C. Clarke, Isaac Asimov, Kim Stanley Robinson",
        "bio": "I write hard science fiction with a focus on realistic space travel, colony ships, and first contact scenarios. I do extensive research to keep the science as accurate as possible (I'm an aerospace engineering student at Imperial College). My stories prioritize plausible technology and the human drama that comes with exploring the cosmos.",
        "total_images": 0,
        "total_comments": 63,
        "gallery_created": "August 30, 2000",
        "last_updated": "May 28, 2002",
        "is_writer": True,
        "stories": [
            {"slug": "drakon-colony-ship", "title": "Colony Ship Meridian", "genre": "Hard Sci-Fi", "words": "19,800", "status": "Chapters 1-7 (In Progress)", "date": "May 28, 2002", "badge": "", "desc": "Three generations into its journey to Proxima Centauri, the colony ship Meridian faces a crisis when its AI navigation system begins making decisions that conflict with human command."},
            {"slug": "drakon-quantum-thief", "title": "The Quantum Thief's Apprentice", "genre": "Space Opera", "words": "6,400", "status": "Complete", "date": "Mar 15, 2002", "badge": "", "desc": "A young pickpocket on a space station is recruited by a legendary thief who can manipulate quantum probability, but the heist they're planning could collapse reality itself."},
        ],
    },
    {
        "slug": "elowen-mist",
        "name": "Elowen Mist",
        "location": "Cardiff, Wales, UK",
        "member_since": "February 1998",
        "media": "Fantasy Fiction",
        "influences": "Diana Wynne Jones, Terry Pratchett, Welsh mythology",
        "bio": "I've been writing fantasy stories since I was ten and posting them on Elfwood since I was sixteen! My stories tend to be lighter in tone - I believe fantasy can be fun and warm without losing its sense of wonder. Welsh mythology features heavily in my work, along with a healthy dose of humour. Currently working on way too many stories at once!",
        "total_images": 0,
        "total_comments": 97,
        "gallery_created": "February 14, 1998",
        "last_updated": "July 2, 2002",
        "is_writer": True,
        "stories": [
            {"slug": "elowen-fey-bargains", "title": "Fey Bargains", "genre": "Urban Fantasy", "words": "4,500", "status": "Complete", "date": "Jul 2, 2002", "badge": "", "desc": "A modern-day Welshwoman accidentally makes a deal with a fairy in a Cardiff supermarket. The fairy's terms are... unusual, to say the least."},
            {"slug": "elowen-cartographer", "title": "The Cartographer's Compass", "genre": "Adventure Fantasy", "words": "22,000", "status": "Chapters 1-8 (In Progress)", "date": "Jun 15, 2002", "badge": "UPDATED!", "desc": "A mapmaker discovers her compass points to places that shouldn't exist. Following it leads her through Welsh mountains into a world where geography itself is alive."},
            {"slug": "elowen-dragon-tea", "title": "Tea with a Dragon", "genre": "Humorous Fantasy", "words": "2,800", "status": "Complete", "date": "May 1, 2002", "badge": "", "desc": "A very proper Welsh grandmother discovers a dragon living in her garden shed. Rather than panicking, she invites it in for tea. The dragon accepts, but has strong opinions about biscuits."},
        ],
    },
]

ALL_ARTISTS = LOTHLORIEN_ARTISTS + ZONE47_ARTISTS + WYVERNS_LIBRARY_AUTHORS

# ============================================================
# SVG GENERATION
# ============================================================

def color_to_rgb(hex_color):
    """Convert hex colour to RGB tuple."""
    h = hex_color.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def darken(hex_color, factor=0.7):
    r, g, b = color_to_rgb(hex_color)
    r2 = int(r * factor)
    g2 = int(g * factor)
    b2 = int(b * factor)
    return f"#{r2:02x}{g2:02x}{b2:02x}"

def lighten(hex_color, factor=0.3):
    r, g, b = color_to_rgb(hex_color)
    r2 = min(255, int(r + (255 - r) * factor))
    g2 = min(255, int(g + (255 - g) * factor))
    b2 = min(255, int(b + (255 - b) * factor))
    return f"#{r2:02x}{g2:02x}{b2:02x}"

def seed_from_slug(slug):
    return int(hashlib.md5(slug.encode()).hexdigest()[:8], 16)

def generate_creature_svg(artwork, width=500, height=375):
    """Generate a unique fantasy SVG illustration."""
    s = seed_from_slug(artwork["slug"])
    random.seed(s)

    bg = artwork["color"]
    bg_dark = darken(bg, 0.5)
    bg_light = lighten(bg, 0.4)
    bg_mid = darken(bg, 0.8)
    accent = lighten(bg, 0.6)

    # Generate deterministic stars
    stars = ""
    for _ in range(random.randint(15, 40)):
        sx = random.randint(0, width)
        sy = random.randint(0, height // 3)
        sr = random.uniform(0.5, 2.0)
        so = random.uniform(0.3, 1.0)
        stars += f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="white" opacity="{so:.1f}"/>\n'

    # Generate mountains/landscape
    mountains = ""
    num_ranges = random.randint(2, 4)
    for i in range(num_ranges):
        base_y = height - random.randint(40, 150) - i * 30
        points = [f"0,{height}"]
        num_peaks = random.randint(3, 7)
        for j in range(num_peaks + 1):
            x = j * width // num_peaks
            y = base_y - random.randint(20, 100)
            points.append(f"{x},{y}")
        points.append(f"{width},{height}")
        mountain_color = darken(bg, 0.6 + i * 0.1)
        mountains += f'<polygon points="{" ".join(points)}" fill="{mountain_color}" opacity="0.8"/>\n'

    # Generate creature silhouette based on slug keywords
    slug = artwork["slug"].lower()
    creature = ""

    if "dragon" in slug or "wyrm" in slug or "wyvern" in slug:
        # Dragon silhouette
        cx, cy = width // 2, height // 2 - 20
        creature = f'''
        <g transform="translate({cx},{cy})">
          <ellipse cx="0" cy="20" rx="60" ry="35" fill="{bg_mid}"/>
          <ellipse cx="-50" cy="5" rx="25" ry="15" fill="{bg_mid}"/>
          <circle cx="-65" cy="-5" r="18" fill="{bg_mid}"/>
          <circle cx="-72" cy="-10" r="3" fill="{accent}"/>
          <path d="M-20,-10 Q-60,-80 -100,-40 Q-70,-50 -30,-15" fill="{bg_mid}" opacity="0.8"/>
          <path d="M20,-10 Q60,-80 100,-40 Q70,-50 30,-15" fill="{bg_mid}" opacity="0.8"/>
          <path d="M50,30 Q80,60 60,80 Q55,50 45,35" fill="{bg_mid}"/>
          <path d="M-60,-15 L-68,-30 M-55,-12 L-60,-25" stroke="{bg_mid}" stroke-width="2" fill="none"/>
        </g>'''
    elif "unicorn" in slug:
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <ellipse cx="0" cy="10" rx="50" ry="30" fill="{bg_mid}"/>
          <ellipse cx="-40" cy="-15" rx="15" ry="20" fill="{bg_mid}"/>
          <line x1="-45" y1="-35" x2="-50" y2="-65" stroke="{accent}" stroke-width="3"/>
          <circle cx="-45" cy="-67" r="3" fill="{accent}"/>
          <path d="M-30,-25 Q-35,-45 -25,-35" fill="{bg_mid}"/>
          <line x1="0" y1="40" x2="-15" y2="70" stroke="{bg_mid}" stroke-width="4"/>
          <line x1="15" y1="40" x2="10" y2="70" stroke="{bg_mid}" stroke-width="4"/>
          <line x1="-20" y1="40" x2="-30" y2="70" stroke="{bg_mid}" stroke-width="4"/>
          <line x1="35" y1="40" x2="30" y2="70" stroke="{bg_mid}" stroke-width="4"/>
          <path d="M45,0 Q90,-20 70,10 Q55,5 45,5" fill="{bg_mid}"/>
        </g>'''
    elif "fairy" in slug or "faerie" in slug or "fey" in slug or "moth" in slug:
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <circle cx="0" cy="-10" r="8" fill="{accent}"/>
          <ellipse cx="0" cy="15" rx="6" ry="18" fill="{accent}"/>
          <path d="M0,0 Q-40,-50 -20,-10" fill="{bg_light}" opacity="0.6" stroke="{accent}" stroke-width="0.5"/>
          <path d="M0,0 Q40,-50 20,-10" fill="{bg_light}" opacity="0.6" stroke="{accent}" stroke-width="0.5"/>
          <path d="M0,5 Q-35,-30 -15,5" fill="{bg_light}" opacity="0.4"/>
          <path d="M0,5 Q35,-30 15,5" fill="{bg_light}" opacity="0.4"/>
          <circle cx="0" cy="-10" r="12" fill="none" stroke="{accent}" stroke-width="0.5" opacity="0.5"/>
          <circle cx="0" cy="-10" r="20" fill="none" stroke="{accent}" stroke-width="0.3" opacity="0.3"/>
        </g>'''
    elif any(k in slug for k in ["mech", "robot", "titan", "drop"]):
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <rect x="-25" y="-40" width="50" height="50" rx="3" fill="{bg_mid}"/>
          <rect x="-20" y="-55" width="40" height="25" rx="5" fill="{bg_mid}"/>
          <rect x="-12" y="-50" width="10" height="6" rx="1" fill="{accent}"/>
          <rect x="2" y="-50" width="10" height="6" rx="1" fill="{accent}"/>
          <rect x="-15" y="10" width="12" height="40" fill="{bg_mid}"/>
          <rect x="3" y="10" width="12" height="40" fill="{bg_mid}"/>
          <rect x="-45" y="-35" width="18" height="10" rx="2" fill="{bg_mid}"/>
          <rect x="27" y="-35" width="18" height="10" rx="2" fill="{bg_mid}"/>
          <rect x="-17" y="50" width="16" height="8" rx="2" fill="{bg_mid}"/>
          <rect x="1" y="50" width="16" height="8" rx="2" fill="{bg_mid}"/>
        </g>'''
    elif any(k in slug for k in ["ship", "station", "fighter", "ark", "dropship"]):
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <path d="M-80,0 Q0,-30 80,0 Q0,15 -80,0" fill="{bg_mid}"/>
          <ellipse cx="0" cy="-5" rx="30" ry="12" fill="{bg_light}" opacity="0.3"/>
          <path d="M-80,0 Q-100,5 -90,10 Q-85,3 -80,0" fill="{accent}" opacity="0.7"/>
          <path d="M80,0 Q100,5 90,10 Q85,3 80,0" fill="{accent}" opacity="0.7"/>
          <circle cx="-10" cy="-3" r="3" fill="{accent}" opacity="0.8"/>
          <circle cx="10" cy="-3" r="3" fill="{accent}" opacity="0.8"/>
        </g>'''
    elif any(k in slug for k in ["castle", "fortress", "tower"]):
        cx = width // 2
        by = height - 80
        creature = f'''
        <g>
          <rect x="{cx-40}" y="{by-80}" width="80" height="120" fill="{bg_mid}"/>
          <rect x="{cx-55}" y="{by-50}" width="30" height="90" fill="{bg_mid}"/>
          <rect x="{cx+25}" y="{by-50}" width="30" height="90" fill="{bg_mid}"/>
          <polygon points="{cx-55},{by-50} {cx-40},{by-70} {cx-25},{by-50}" fill="{darken(bg, 0.6)}"/>
          <polygon points="{cx+25},{by-50} {cx+40},{by-70} {cx+55},{by-50}" fill="{darken(bg, 0.6)}"/>
          <polygon points="{cx-40},{by-80} {cx},{by-110} {cx+40},{by-80}" fill="{darken(bg, 0.6)}"/>
          <rect x="{cx-8}" y="{by}" width="16" height="25" fill="{darken(bg, 0.4)}"/>
          <rect x="{cx-50}" y="{by-45}" width="6" height="8" fill="{accent}" opacity="0.7"/>
          <rect x="{cx-30}" y="{by-70}" width="6" height="8" fill="{accent}" opacity="0.7"/>
          <rect x="{cx+24}" y="{by-70}" width="6" height="8" fill="{accent}" opacity="0.7"/>
          <rect x="{cx+44}" y="{by-45}" width="6" height="8" fill="{accent}" opacity="0.7"/>
        </g>'''
    elif any(k in slug for k in ["knight", "warrior", "sorceress", "queen", "witch", "woman", "angel"]):
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <circle cx="0" cy="-35" r="12" fill="{bg_mid}"/>
          <path d="M-12,-23 L-18,20 L18,20 L12,-23" fill="{bg_mid}"/>
          <line x1="-18" y1="20" x2="-22" y2="60" stroke="{bg_mid}" stroke-width="5"/>
          <line x1="18" y1="20" x2="22" y2="60" stroke="{bg_mid}" stroke-width="5"/>
          <path d="M-12,-15 Q-35,-5 -40,10" stroke="{bg_mid}" stroke-width="3" fill="none"/>
          <path d="M12,-15 Q35,-5 40,10" stroke="{bg_mid}" stroke-width="3" fill="none"/>
          <circle cx="0" cy="-35" r="18" fill="none" stroke="{accent}" stroke-width="0.5" opacity="0.4"/>
        </g>'''
    elif any(k in slug for k in ["giant", "golem", "elemental", "frost"]):
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <ellipse cx="0" cy="10" rx="45" ry="50" fill="{bg_mid}"/>
          <circle cx="0" cy="-40" r="25" fill="{bg_mid}"/>
          <circle cx="-8" cy="-45" r="4" fill="{accent}"/>
          <circle cx="8" cy="-45" r="4" fill="{accent}"/>
          <rect x="-55" y="-20" width="20" height="50" rx="8" fill="{bg_mid}"/>
          <rect x="35" y="-20" width="20" height="50" rx="8" fill="{bg_mid}"/>
          <rect x="-25" y="55" width="18" height="30" rx="5" fill="{bg_mid}"/>
          <rect x="7" y="55" width="18" height="30" rx="5" fill="{bg_mid}"/>
        </g>'''
    elif any(k in slug for k in ["whale", "serpent", "kelpie", "selkie", "sea"]):
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <path d="M-80,0 Q-40,-30 0,-10 Q40,10 80,-20 Q60,0 40,10 Q0,30 -40,20 Q-70,10 -80,0" fill="{bg_mid}"/>
          <circle cx="-60" cy="-8" r="4" fill="{accent}"/>
          <path d="M75,-18 Q100,-35 85,-10" fill="{bg_mid}" opacity="0.7"/>
        </g>'''
    elif any(k in slug for k in ["hedgehog", "mouse", "bird", "deer"]):
        cx, cy = width // 2, height // 2 + 20
        creature = f'''
        <g transform="translate({cx},{cy})">
          <ellipse cx="0" cy="0" rx="25" ry="18" fill="{bg_mid}"/>
          <circle cx="-18" cy="-10" r="10" fill="{bg_mid}"/>
          <circle cx="-22" cy="-13" r="2.5" fill="{accent}"/>
          <path d="M-25,-13 L-32,-15 L-28,-11" fill="{bg_mid}"/>
          <circle cx="0" cy="0" r="30" fill="none" stroke="{accent}" stroke-width="0.5" opacity="0.3"/>
        </g>'''
    elif any(k in slug for k in ["phoenix", "fire"]):
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <circle cx="0" cy="-5" r="12" fill="{bg_mid}"/>
          <ellipse cx="0" cy="20" rx="15" ry="25" fill="{bg_mid}"/>
          <path d="M-10,5 Q-70,-40 -50,20" fill="{accent}" opacity="0.6"/>
          <path d="M10,5 Q70,-40 50,20" fill="{accent}" opacity="0.6"/>
          <path d="M0,45 Q-20,80 -10,100 Q0,70 10,100 Q20,80 0,45" fill="{accent}" opacity="0.5"/>
          <circle cx="-4" cy="-8" r="2" fill="{accent}"/>
          <circle cx="4" cy="-8" r="2" fill="{accent}"/>
        </g>'''
    elif any(k in slug for k in ["garden", "cave", "crystal", "island", "floating"]):
        cx = width // 2
        by = height // 2
        creature = f'''
        <g>
          <ellipse cx="{cx}" cy="{by+20}" rx="100" ry="40" fill="{bg_mid}" opacity="0.5"/>
          <circle cx="{cx-30}" cy="{by-10}" r="20" fill="{bg_light}" opacity="0.4"/>
          <circle cx="{cx+20}" cy="{by}" r="25" fill="{bg_light}" opacity="0.3"/>
          <circle cx="{cx}" cy="{by-25}" r="15" fill="{bg_light}" opacity="0.35"/>
          <circle cx="{cx-10}" cy="{by+5}" r="8" fill="{accent}" opacity="0.5"/>
          <circle cx="{cx+25}" cy="{by-15}" r="6" fill="{accent}" opacity="0.5"/>
          <circle cx="{cx-25}" cy="{by+15}" r="5" fill="{accent}" opacity="0.4"/>
        </g>'''
    else:
        # Generic magical scene
        cx, cy = width // 2, height // 2
        creature = f'''
        <g transform="translate({cx},{cy})">
          <circle cx="0" cy="0" r="40" fill="{bg_mid}" opacity="0.5"/>
          <circle cx="0" cy="0" r="30" fill="{bg_light}" opacity="0.3"/>
          <circle cx="0" cy="0" r="20" fill="{accent}" opacity="0.2"/>
          <path d="M0,-40 L5,-10 L35,-25 L10,0 L40,15 L5,10 L0,40 L-5,10 L-40,15 L-10,0 L-35,-25 L-5,-10 Z" fill="{accent}" opacity="0.4"/>
        </g>'''

    # Moon or sun
    is_night = random.random() > 0.4
    celestial = ""
    if is_night:
        mx = random.randint(width // 4, 3 * width // 4)
        my = random.randint(30, height // 4)
        celestial = f'''
        <circle cx="{mx}" cy="{my}" r="25" fill="{lighten(bg, 0.7)}" opacity="0.8"/>
        <circle cx="{mx+8}" cy="{my-5}" r="25" fill="{bg_dark}"/>'''
    else:
        mx = random.randint(width // 4, 3 * width // 4)
        my = random.randint(30, height // 4)
        celestial = f'''
        <circle cx="{mx}" cy="{my}" r="20" fill="{accent}" opacity="0.9"/>
        <circle cx="{mx}" cy="{my}" r="30" fill="{accent}" opacity="0.2"/>
        <circle cx="{mx}" cy="{my}" r="45" fill="{accent}" opacity="0.1"/>'''

    title_escaped = artwork["title"].replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;").replace("'", "&apos;")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="sky-{artwork['slug']}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{bg_dark}"/>
      <stop offset="60%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{bg_light}"/>
    </linearGradient>
  </defs>
  <rect width="{width}" height="{height}" fill="url(#sky-{artwork['slug']})"/>
  {stars}
  {celestial}
  {mountains}
  {creature}
  <text x="{width//2}" y="{height - 15}" text-anchor="middle" fill="{accent}" font-family="Georgia, serif" font-size="12" font-style="italic" opacity="0.8">{title_escaped}</text>
</svg>'''
    return svg


def generate_thumbnail_svg(artwork, width=100, height=75):
    """Generate a smaller thumbnail version."""
    s = seed_from_slug(artwork["slug"])
    random.seed(s)

    bg = artwork["color"]
    bg_dark = darken(bg, 0.5)
    bg_light = lighten(bg, 0.4)
    bg_mid = darken(bg, 0.7)
    accent = lighten(bg, 0.6)

    # Simplified version - just gradient background with a small silhouette hint
    stars = ""
    for _ in range(random.randint(5, 12)):
        sx = random.randint(0, width)
        sy = random.randint(0, height // 2)
        sr = random.uniform(0.3, 1.0)
        stars += f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="white" opacity="0.5"/>\n'

    # Simple mountain
    points = f"0,{height} "
    for i in range(5):
        x = i * width // 4
        y = height - random.randint(15, 40)
        points += f"{x},{y} "
    points += f"{width},{height}"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="{bg}"/>
  <rect width="{width}" height="{height//2}" fill="{bg_dark}" opacity="0.3"/>
  {stars}
  <polygon points="{points}" fill="{bg_mid}" opacity="0.6"/>
  <circle cx="{width//2}" cy="{height//2 - 5}" r="12" fill="{bg_mid}" opacity="0.7"/>
  <circle cx="{width//2}" cy="{height//2 - 5}" r="8" fill="{accent}" opacity="0.3"/>
</svg>'''
    return svg


def generate_profile_svg(artist_slug, width=100, height=100):
    """Generate a simple profile portrait SVG."""
    s = seed_from_slug(artist_slug)
    random.seed(s)

    # Deterministic colour from slug
    hue_seed = s % 360
    bg_r = 100 + (s % 80)
    bg_g = 80 + ((s >> 8) % 80)
    bg_b = 100 + ((s >> 16) % 80)
    bg = f"#{bg_r:02x}{bg_g:02x}{bg_b:02x}"
    bg_light = f"#{min(255,bg_r+60):02x}{min(255,bg_g+60):02x}{min(255,bg_b+60):02x}"
    skin = f"#{180 + (s%40):02x}{150 + (s%30):02x}{130 + (s%30):02x}"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="{bg}"/>
  <circle cx="50" cy="38" r="18" fill="{skin}"/>
  <path d="M30,65 Q30,45 50,42 Q70,45 70,65 L70,100 L30,100 Z" fill="{bg_light}"/>
  <circle cx="44" cy="35" r="2" fill="#333"/>
  <circle cx="56" cy="35" r="2" fill="#333"/>
  <path d="M47,42 Q50,45 53,42" fill="none" stroke="#333" stroke-width="1"/>
  <path d="M32,28 Q50,{15 + s%15} 68,28" fill="{darken(bg, 0.6)}" opacity="0.8"/>
</svg>'''
    return svg


# ============================================================
# HTML PAGE GENERATION
# ============================================================

HEADER_NAV = '''<a class="skip-nav" href="#main-content">Skip to main content</a>

<table class="page-wrapper" cellpadding="0" cellspacing="0" border="0" role="presentation">

  <!-- Header -->
  <tr>
    <td>
      <table class="header-table" cellpadding="0" cellspacing="0" border="0" role="presentation">
        <tr>
          <td>
            <div class="site-title"><a href="index.html">&#9733; DOLLYWOODS &#9733;</a></div>
            <div class="site-subtitle">Where Elfwood Meets Dollywood &mdash; Fantasy, Sci-Fi, Rhinestones &amp; Big Hair</div>
          </td>
        </tr>
      </table>
    </td>
  </tr>

  <!-- Navigation -->
  <tr>
    <td>
      <table class="nav-table" cellpadding="0" cellspacing="0" border="0" role="navigation" aria-label="Main navigation">
        <tr>
          <td>
            <a href="lothlorien.html">Lothlorien</a>
            <span class="nav-separator">|</span>
            <a href="zone47.html">Zone 47</a>
            <span class="nav-separator">|</span>
            <a href="wyverns-library.html">Wyvern\'s Library</a>
            <span class="nav-separator">|</span>
            <a href="fanquarter.html">Fan Quarter</a>
            <span class="nav-separator">|</span>
            <a href="farp.html">FARP</a>
            <span class="nav-separator">|</span>
            <a href="index.html">Front Porch</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>'''

FOOTER = '''  <!-- Footer -->
  <tr>
    <td>
      <table class="footer-table" cellpadding="0" cellspacing="0" border="0" role="contentinfo">
        <tr>
          <td>
            <strong style="color: #ffd700;">DOLLYWOODS</strong>&trade; &mdash; All artwork &copy; their respective creators. Y'all be good now!<br>
            <a href="index.html">Home</a> |
            <a href="lothlorien.html">Lothlorien</a> |
            <a href="zone47.html">Zone 47</a> |
            <a href="wyverns-library.html">Wyvern\'s Library</a> |
            <a href="fanquarter.html">Fan Quarter</a> |
            <a href="farp.html">FARP</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>

</table>

</body>
</html>'''


COMMENT_AUTHORS = [
    ("Jolene Starfire", "This is absolutely stunning work! The colours are gorgeous and the composition draws you right in. I've been following your gallery for months and you just keep getting better!"),
    ("Rhinestone Ranger", "Well, I'll be! This is prettier than a sunset over Dollywood! The detail work here is incredible, especially the textures. You've got real talent, sugar!"),
    ("Tennessee Dreamer", "Found your gallery through the homepage and I am NOT disappointed! This piece made me feel things. The mood, the atmosphere, everything is just perfect."),
    ("Mountain Mama", "As a fellow artist, I just wanna say your technique is top-notch. The way you handle light and shadow is something I aspire to. Keep creating, darlin'!"),
    ("Glitter Goblin", "YESSSSS! This is everything I wanted and more! The creativity here is off the charts. Would love to see more work in this style!"),
    ("Butterscotch Belle", "I'm new to Elfwood and this gallery is making me want to start creating my own art! You're such an inspiration. Beautiful, beautiful work!"),
    ("Starlight Sage", "The storytelling in this piece is remarkable. Every detail adds to the narrative. I could stare at this for hours and keep finding new things."),
    ("Crystal Moonbeam", "Oh my stars! This is the most beautiful thing I've seen this week. Your use of colour theory is impeccable. Absolutely breathtaking!"),
]


def get_section(artist):
    return artist.get("section", "lothlorien")


def get_section_name(artist):
    sec = get_section(artist)
    return {"lothlorien": "Lothlorien", "zone47": "Zone 47", "wyverns-library": "Wyvern's Library"}.get(sec, "Lothlorien")


def get_section_link(artist):
    sec = get_section(artist)
    return {"lothlorien": "lothlorien.html", "zone47": "zone47.html", "wyverns-library": "wyverns-library.html"}.get(sec, "lothlorien.html")


def generate_artist_page(artist):
    """Generate a unique artist profile page."""
    name = artist["name"]
    slug = artist["slug"]
    section_name = get_section_name(artist)
    section_link = get_section_link(artist)
    is_writer = artist.get("is_writer", False)
    items = artist.get("stories", artist.get("artworks", []))

    # Generate comments
    s = seed_from_slug(slug)
    random.seed(s)
    comment_indices = random.sample(range(len(COMMENT_AUTHORS)), min(4, len(COMMENT_AUTHORS)))

    comments_html = ""
    months = ["July", "June", "May", "April"]
    for i, ci in enumerate(comment_indices):
        author, text = COMMENT_AUTHORS[ci]
        day = random.randint(1, 28)
        hour = random.randint(8, 23)
        minute = random.randint(0, 59)
        month = months[min(i, len(months)-1)]
        comments_html += f'''
      <div class="comment-box">
        <span class="comment-author">{author}</span>
        <span class="comment-date">&mdash; {month} {day}, 2002, {hour:02d}:{minute:02d}</span>
        <div class="comment-text">{text}</div>
      </div>
'''

    if is_writer:
        # Writer profile with story list
        stories_html = ""
        for story in items:
            badge = f' <span class="badge-new">{story["badge"]}</span>' if story.get("badge") else ""
            stories_html += f'''
        <div style="padding: 8px; margin-bottom: 6px; background-color: #fff0f5; border: 1px solid #e8a0c8;">
          <a href="{story['slug']}.html"><strong>{story['title']}</strong></a>
          <span class="genre-tag">{story['genre']}</span>{badge}<br>
          <span class="story-info">{story['words']} words &mdash; {story['status']}</span><br>
          <span style="font-size: 10px; color: #666666;">{story['desc']}</span>
        </div>
'''

        items_section = f'''
      <div class="section-subheader">Stories &amp; Writing</div>
      {stories_html}
      <p style="font-size: 10px; color: #666666; text-align: center;">
        Showing all {len(items)} stories.
      </p>'''
    else:
        # Artist profile with artwork thumbnails
        thumbs_html = '<table class="thumb-table" cellpadding="0" cellspacing="0" border="0">\n'
        for i, aw in enumerate(items):
            if i % 4 == 0:
                if i > 0:
                    thumbs_html += "        </tr>\n"
                thumbs_html += "        <tr>\n"
            badge = f' <span class="badge-new">{aw["badge"]}</span>' if aw.get("badge") else ""
            thumbs_html += f'''          <td>
            <a href="{aw['slug']}.html">
              <img src="images/{aw['slug']}-thumb.svg" alt="{aw['title']}" width="100" height="75" style="border: 2px solid #cc88aa;">
            </a>
            <div class="thumb-title"><a href="{aw['slug']}.html">{aw['title']}</a></div>
            <div class="thumb-info">{aw['medium']}<br>{aw['date']}{badge}</div>
          </td>
'''
        # Close last row
        remainder = len(items) % 4
        if remainder != 0:
            for _ in range(4 - remainder):
                thumbs_html += "          <td></td>\n"
        thumbs_html += "        </tr>\n      </table>"

        items_section = f'''
      <div class="section-subheader">Artwork Gallery</div>
      {thumbs_html}
      <p style="font-size: 10px; color: #666666; text-align: center;">
        Showing {len(items)} of {artist['total_images']} artworks.
      </p>'''

    item_type = "stories" if is_writer else "images"
    item_count = len(items) if is_writer else artist["total_images"]

    page = f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
  <title>Elfwood - {name}'s Gallery</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
{HEADER_NAV}

  <!-- Main Content -->
  <tr>
    <td style="padding: 10px 15px; background-color: #f5f0e0;" id="main-content">

      <div class="breadcrumb">
        <a href="index.html">Elfwood</a> &raquo;
        <a href="{section_link}">{section_name}</a> &raquo;
        <strong>{name}'s Gallery</strong>
      </div>

      <hr>

      <!-- Artist Bio -->
      <table cellpadding="0" cellspacing="0" border="0" width="100%" role="presentation">
        <tr>
          <td>
            <div class="section-header" style="font-size: 20px;">{name}'s {"Writing" if is_writer else "Fantasy Art"} Gallery</div>
          </td>
        </tr>
      </table>

      <div class="bio-box">
        <table cellpadding="0" cellspacing="0" border="0" width="100%" role="presentation">
          <tr>
            <td style="width: 120px; vertical-align: top; padding-right: 10px;">
              <img src="images/{slug}-profile.svg" alt="Portrait of {name}" width="100" height="100" style="border: 2px solid #cc88aa;">
            </td>
            <td style="vertical-align: top;">
              <span class="bio-label">Name:</span> {name}<br>
              <span class="bio-label">Location:</span> {artist['location']}<br>
              <span class="bio-label">Member Since:</span> {artist['member_since']}<br>
              <span class="bio-label">{'Writes' if is_writer else 'Favourite Media'}:</span> {artist['media']}<br>
              <span class="bio-label">Influences:</span> {artist['influences']}<br>
              <br>
              <span style="font-size: 11px; line-height: 1.5;">{artist['bio']}</span>
            </td>
          </tr>
        </table>
        <div style="font-size: 9px; color: #999999; margin-top: 6px; text-align: right;">
          Gallery created: {artist['gallery_created']} | Last updated: {artist['last_updated']} | {item_count} {item_type} | {artist['total_comments']} comments received
        </div>
      </div>

      <hr>

      {items_section}

      <hr>

      <!-- Comments -->
      <div class="section-subheader">Recent Comments</div>
      {comments_html}

      <hr>

      <p style="text-align: center; font-size: 11px;">
        <a href="{section_link}">&laquo; Back to {section_name}</a>
        &nbsp;|&nbsp;
        <a href="index.html">Back to Elfwood Home</a>
      </p>

    </td>
  </tr>

{FOOTER}'''

    return page


def generate_artwork_page(artist, artwork, artwork_index):
    """Generate an artwork detail page."""
    name = artist["name"]
    slug = artist["slug"]
    aw_slug = artwork["slug"]
    section_name = get_section_name(artist)
    section_link = get_section_link(artist)
    items = artist.get("artworks", [])
    total = artist["total_images"]

    # Prev/Next navigation
    prev_link = ""
    next_link = ""
    if artwork_index > 0:
        prev_aw = items[artwork_index - 1]
        prev_link = f'<a href="{prev_aw["slug"]}.html">&laquo; Previous: "{prev_aw["title"]}"</a>'
    else:
        prev_link = '<span style="color: #999999;">This is the first artwork</span>'

    if artwork_index < len(items) - 1:
        next_aw = items[artwork_index + 1]
        next_link = f'<a href="{next_aw["slug"]}.html">Next: "{next_aw["title"]}" &raquo;</a>'
    else:
        next_link = '<span style="color: #999999;">This is the newest artwork</span>'

    # Generate comments
    s = seed_from_slug(aw_slug)
    random.seed(s)
    comment_indices = random.sample(range(len(COMMENT_AUTHORS)), min(3, len(COMMENT_AUTHORS)))

    comments_html = ""
    months = ["July", "June", "May"]
    for i, ci in enumerate(comment_indices):
        author, text = COMMENT_AUTHORS[ci]
        day = random.randint(1, 28)
        hour = random.randint(8, 23)
        minute = random.randint(0, 59)
        month = months[min(i, len(months)-1)]
        comments_html += f'''
      <div class="comment-box">
        <span class="comment-author">{author}</span>
        <span class="comment-date">&mdash; {month} {day}, 2002, {hour:02d}:{minute:02d}</span>
        <div class="comment-text">{text}</div>
      </div>
'''

    views = random.randint(100, 900)
    num_comments = random.randint(3, 15)

    page = f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
  <title>Elfwood - "{artwork['title']}" by {name}</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
{HEADER_NAV}

  <!-- Main Content -->
  <tr>
    <td style="padding: 10px 15px; background-color: #f5f0e0;" id="main-content">

      <div class="breadcrumb">
        <a href="index.html">Elfwood</a> &raquo;
        <a href="{section_link}">{section_name}</a> &raquo;
        <a href="{slug}.html">{name}</a> &raquo;
        <strong>{artwork['title']}</strong>
      </div>

      <hr>

      <!-- Prev/Next Navigation -->
      <table cellpadding="0" cellspacing="0" border="0" width="100%" role="navigation" aria-label="Artwork navigation">
        <tr>
          <td style="width: 33%; text-align: left; font-size: 10px;">
            {prev_link}
          </td>
          <td style="width: 34%; text-align: center; font-size: 10px;">
            <a href="{slug}.html">Back to Gallery</a> ({artwork_index + 1} of {total})
          </td>
          <td style="width: 33%; text-align: right; font-size: 10px;">
            {next_link}
          </td>
        </tr>
      </table>

      <hr>

      <!-- Artwork Display -->
      <div style="text-align: center; margin: 15px 0;">
        <div class="section-header" style="font-size: 18px; text-align: center; border-bottom: none;">
          "{artwork['title']}"
        </div>
        <div style="font-size: 11px; color: #666666; margin-bottom: 10px;">
          by <a href="{slug}.html"><strong>{name}</strong></a>
        </div>

        <img src="images/{aw_slug}.svg" alt="{artwork['desc']}" width="500" height="375" style="border: 2px solid #cc88aa;">
      </div>

      <!-- Artwork Details -->
      <div class="bio-box">
        <table cellpadding="2" cellspacing="0" border="0" role="presentation">
          <tr>
            <td class="bio-label" style="padding-right: 10px;">Title:</td>
            <td>{artwork['title']}</td>
          </tr>
          <tr>
            <td class="bio-label" style="padding-right: 10px;">Artist:</td>
            <td><a href="{slug}.html">{name}</a></td>
          </tr>
          <tr>
            <td class="bio-label" style="padding-right: 10px;">Date:</td>
            <td>{artwork['date']}</td>
          </tr>
          <tr>
            <td class="bio-label" style="padding-right: 10px;">Medium:</td>
            <td>{artwork['medium']}</td>
          </tr>
          <tr>
            <td class="bio-label" style="padding-right: 10px; vertical-align: top;">Description:</td>
            <td style="line-height: 1.5;">{artwork['desc']}</td>
          </tr>
        </table>
        <div style="font-size: 9px; color: #999999; margin-top: 8px; text-align: right;">
          Views: {views} | Comments: {num_comments}
        </div>
      </div>

      <hr>

      <!-- Comments -->
      <div class="section-header">Reader Comments ({num_comments})</div>
      {comments_html}

      <hr>

      <!-- Bottom Navigation -->
      <table cellpadding="0" cellspacing="0" border="0" width="100%" role="navigation" aria-label="Artwork navigation">
        <tr>
          <td style="width: 33%; text-align: left; font-size: 10px;">
            {prev_link}
          </td>
          <td style="width: 34%; text-align: center; font-size: 10px;">
            <a href="{slug}.html">Back to Gallery</a>
          </td>
          <td style="width: 33%; text-align: right; font-size: 10px;">
            {next_link}
          </td>
        </tr>
      </table>

    </td>
  </tr>

{FOOTER}'''

    return page


def generate_story_page(artist, story):
    """Generate a story detail page for writers."""
    name = artist["name"]
    slug = artist["slug"]
    st_slug = story["slug"]
    section_name = "Wyvern's Library"
    section_link = "wyverns-library.html"

    # Generate sample story text
    s = seed_from_slug(st_slug)
    random.seed(s)

    # Generate comments
    comment_indices = random.sample(range(len(COMMENT_AUTHORS)), min(3, len(COMMENT_AUTHORS)))

    comments_html = ""
    months = ["July", "June", "May"]
    for i, ci in enumerate(comment_indices):
        author, text = COMMENT_AUTHORS[ci]
        day = random.randint(1, 28)
        hour = random.randint(8, 23)
        minute = random.randint(0, 59)
        month = months[min(i, len(months)-1)]
        comments_html += f'''
      <div class="comment-box">
        <span class="comment-author">{author}</span>
        <span class="comment-date">&mdash; {month} {day}, 2002, {hour:02d}:{minute:02d}</span>
        <div class="comment-text">{text}</div>
      </div>
'''

    reads = random.randint(200, 1200)
    num_comments = random.randint(5, 20)

    page = f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
  <title>Elfwood - "{story['title']}" by {name}</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
{HEADER_NAV}

  <!-- Main Content -->
  <tr>
    <td style="padding: 10px 15px; background-color: #f5f0e0;" id="main-content">

      <div class="breadcrumb">
        <a href="index.html">Elfwood</a> &raquo;
        <a href="{section_link}">{section_name}</a> &raquo;
        <a href="{slug}.html">{name}</a> &raquo;
        <strong>{story['title']}</strong>
      </div>

      <hr>

      <div class="section-header" style="font-size: 18px; text-align: center; border-bottom: none;">
        "{story['title']}"
      </div>
      <div style="font-size: 11px; color: #666666; margin-bottom: 10px; text-align: center;">
        by <a href="{slug}.html"><strong>{name}</strong></a>
        &mdash; <span class="genre-tag">{story['genre']}</span>
        &mdash; {story['words']} words &mdash; {story['status']}
      </div>

      <hr>

      <!-- Story Details -->
      <div class="bio-box">
        <p style="line-height: 1.6; font-size: 11px;">
          <strong>Synopsis:</strong> {story['desc']}
        </p>
        <p style="line-height: 1.6; font-size: 11px; font-style: italic; color: #666666;">
          This story is hosted on Elfwood's Wyvern's Library. To read the full text,
          you would normally click through to the story chapters. In our recreation of
          Elfwood circa 2002, we invite you to imagine the tale unfolding before you,
          each word crafted with care by {name} for your enjoyment.
        </p>
        <div style="font-size: 9px; color: #999999; margin-top: 8px; text-align: right;">
          Reads: {reads} | Comments: {num_comments} | Last updated: {story['date']}
        </div>
      </div>

      <hr>

      <!-- Comments -->
      <div class="section-header">Reader Comments ({num_comments})</div>
      {comments_html}

      <hr>

      <p style="text-align: center; font-size: 11px;">
        <a href="{slug}.html">&laquo; Back to {name}'s Gallery</a>
        &nbsp;|&nbsp;
        <a href="{section_link}">Back to {section_name}</a>
        &nbsp;|&nbsp;
        <a href="index.html">Back to Elfwood Home</a>
      </p>

    </td>
  </tr>

{FOOTER}'''

    return page


# ============================================================
# MAIN GENERATION
# ============================================================

def main():
    print("Generating DOLLYWOODS site content...")

    file_count = 0

    for artist in ALL_ARTISTS:
        slug = artist["slug"]
        is_writer = artist.get("is_writer", False)

        # Generate profile SVG
        profile_svg = generate_profile_svg(slug)
        profile_path = os.path.join(IMG_DIR, f"{slug}-profile.svg")
        with open(profile_path, "w") as f:
            f.write(profile_svg)
        file_count += 1

        # Generate artist page
        artist_page = generate_artist_page(artist)
        artist_path = os.path.join(BASE_DIR, f"{slug}.html")
        with open(artist_path, "w") as f:
            f.write(artist_page)
        file_count += 1

        if is_writer:
            # Generate story pages
            for story in artist.get("stories", []):
                story_page = generate_story_page(artist, story)
                story_path = os.path.join(BASE_DIR, f"{story['slug']}.html")
                with open(story_path, "w") as f:
                    f.write(story_page)
                file_count += 1
        else:
            # Generate artwork SVGs and pages
            for i, artwork in enumerate(artist.get("artworks", [])):
                # Full-size SVG
                full_svg = generate_creature_svg(artwork)
                full_path = os.path.join(IMG_DIR, f"{artwork['slug']}.svg")
                with open(full_path, "w") as f:
                    f.write(full_svg)
                file_count += 1

                # Thumbnail SVG
                thumb_svg = generate_thumbnail_svg(artwork)
                thumb_path = os.path.join(IMG_DIR, f"{artwork['slug']}-thumb.svg")
                with open(thumb_path, "w") as f:
                    f.write(thumb_svg)
                file_count += 1

                # Artwork detail page
                artwork_page = generate_artwork_page(artist, artwork, i)
                artwork_path = os.path.join(BASE_DIR, f"{artwork['slug']}.html")
                with open(artwork_path, "w") as f:
                    f.write(artwork_page)
                file_count += 1

    print(f"Generated {file_count} files!")

    # Print summary
    artist_count = len(ALL_ARTISTS)
    artwork_count = sum(len(a.get("artworks", [])) for a in ALL_ARTISTS if not a.get("is_writer"))
    story_count = sum(len(a.get("stories", [])) for a in ALL_ARTISTS if a.get("is_writer"))
    print(f"  {artist_count} artist/author profile pages")
    print(f"  {artwork_count} artwork detail pages with SVG images")
    print(f"  {story_count} story detail pages")


if __name__ == "__main__":
    main()
