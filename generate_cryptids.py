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
        "influences": "John Keel, Appalachian folklore, abandoned industrial architecture, storm photography",
        "bio": "I live ten minutes from the Silver Bridge and I've been drawing the Mothman since before I could spell his name. My art explores the strange and unexplained creatures that lurk in the hollers and ridges of Appalachia and beyond. If you've ever seen a pair of red eyes glowin' back at you from the treeline at dusk, you'll understand my work. Not sayin' I've seen him personally. Not sayin' I haven't, neither.",
        "total_images": 19,
        "total_comments": 104,
        "gallery_created": "October 31, 1998",
        "last_updated": "July 14, 2002",
        "artworks": [
            {"slug": "molly-mothman-bridge", "title": "Mothman on the Silver Bridge", "medium": "Charcoal &amp; Red Pastel", "date": "Jul 14, 2002", "badge": "NEW!", "color": "#3a2233", "desc": "A towering winged figure with blazing red eyes perched on the cables of the Silver Bridge at Point Pleasant, West Virginia. The Ohio River churns black below. Rendered in stark charcoal with only the creature's eyes in blood-red pastel."},
            {"slug": "molly-flatwoods-monster", "title": "The Flatwoods Monster", "medium": "Pastel &amp; Digital", "date": "Jun 22, 2002", "badge": "", "color": "#224422", "desc": "The Braxton County Monster hoverin' above a misty West Virginia hillside, its ace-of-spades-shaped head glowin' green, long clawed fingers reachin' out from a pleated metal skirt. A group of terrified children flee down the path below."},
            {"slug": "molly-wampus-cat", "title": "The Wampus Cat Prowls", "medium": "Charcoal &amp; Pastel", "date": "May 30, 2002", "badge": "", "color": "#554433", "desc": "A six-legged panther-like beast with glowing amber eyes stalking through moonlit Appalachian underbrush. Cherokee legend says it's a woman cursed for spying on sacred rituals. The detail in the fur and the forest floor is somethin' else."},
            {"slug": "molly-mothman-prophecy", "title": "Red Eyes Over the Holler", "medium": "Digital &amp; Charcoal", "date": "Apr 15, 2002", "badge": "", "color": "#2a1122", "desc": "A panoramic view of a misty Appalachian valley at twilight. Two enormous red eyes glow from the ridgeline above a small cluster of houses. Every window in the holler is dark except one, where a figure stands watching."},
        ],
    },
    {
        "slug": "sasquatch-sam",
        "name": "Sasquatch Sam",
        "location": "Olympia, Washington, USA",
        "member_since": "March 2000",
        "media": "Oils, Gouache",
        "influences": "Patterson-Gimlin film, Pacific Northwest landscape painting, Albert Bierstadt, National Park posters",
        "bio": "I paint Bigfoot. That's what I do. Some people think that's funny, and I get it, but hear me out: the Pacific Northwest is already the most beautiful and mysterious landscape on Earth. Add a giant undiscovered primate to it and you've got the greatest subject matter any painter could ask for. I hike deep into the Cascades and Olympics for reference, and if my paintings look real, it's because the forests ARE that eerie. I have not found Bigfoot yet. But I've found his paintings.",
        "total_images": 14,
        "total_comments": 78,
        "gallery_created": "March 15, 2000",
        "last_updated": "July 10, 2002",
        "artworks": [
            {"slug": "sam-sasquatch-creek", "title": "Sasquatch at the Creek Crossing", "medium": "Oils", "date": "Jul 10, 2002", "badge": "NEW!", "color": "#3a4a2a", "desc": "A massive, shaggy figure mid-stride crossing a misty Pacific Northwest creek, one enormous hand reaching for a moss-covered boulder. Old-growth cedars tower overhead. The creature is half-hidden in morning fog, just detailed enough to be undeniable."},
            {"slug": "sam-bigfoot-family", "title": "The Family on Ape Canyon Ridge", "medium": "Oils &amp; Gouache", "date": "Jun 18, 2002", "badge": "", "color": "#445533", "desc": "Three Sasquatch figures &mdash; an adult, a juvenile, and a smaller youngster &mdash; silhouetted on a rocky ridge at sunset, the volcanic peak of Mt. St. Helens visible in the smoky distance. Inspired by the 1924 Ape Canyon incident."},
            {"slug": "sam-pnw-nightwatch", "title": "The Night Watcher", "medium": "Oils", "date": "May 5, 2002", "badge": "", "color": "#2a3322", "desc": "Painted from the perspective of a camper looking out of a tent at night. Flashlight beam illuminates rain-soaked ferns and, just barely visible between massive tree trunks, a pair of reflective eyes eight feet off the ground."},
            {"slug": "sam-bigfoot-snow", "title": "Tracks in First Snow", "medium": "Gouache", "date": "Mar 28, 2002", "badge": "", "color": "#889999", "desc": "A trail of enormous footprints crossing a pristine snowfield in the North Cascades, leading toward a dark treeline. One print is shown in perfect detail in the foreground. No creature visible &mdash; just the undeniable evidence."},
        ],
    },
    {
        "slug": "jersey-pine",
        "name": "Jersey Pine",
        "location": "Hammonton, New Jersey, USA",
        "member_since": "January 2001",
        "media": "Ink, Watercolour",
        "influences": "Edward Gorey, colonial American folk art, Pine Barrens ecology, Victorian cryptozoology illustrations",
        "bio": "I grew up on the edge of the Pine Barrens and my grandmother swore on a stack of Bibles she saw the Jersey Devil when she was nine years old. That story shaped my entire artistic life. I illustrate cryptids in the style of Victorian-era naturalist field guides &mdash; as if these creatures were simply undiscovered species waiting to be catalogued. Ink and watercolour on aged paper. Every creature gets the scientific treatment it deserves.",
        "total_images": 16,
        "total_comments": 91,
        "gallery_created": "January 20, 2001",
        "last_updated": "July 8, 2002",
        "artworks": [
            {"slug": "pine-jersey-devil", "title": "Cryptid Field Guide: Leeds Devil", "medium": "Ink &amp; Watercolour", "date": "Jul 8, 2002", "badge": "UPDATED!", "color": "#887755", "desc": "A meticulously detailed naturalist illustration of the Jersey Devil in the style of an 18th-century field guide. Multiple anatomical views showing the bat wings, forked tail, horse-like head, and cloven hooves. Handwritten Latin classification and habitat notes in the margins."},
            {"slug": "pine-thunderbird-plate", "title": "Cryptid Field Guide: Thunderbird", "medium": "Ink &amp; Watercolour", "date": "Jun 15, 2002", "badge": "", "color": "#998866", "desc": "A Victorian naturalist plate depicting the great Thunderbird in flight, wingspan measurements annotated in the margins. Below, a size comparison with a bald eagle and a human figure. Beautifully aged paper effect with coffee stains and field notes."},
            {"slug": "pine-champ-specimen", "title": "Cryptid Field Guide: Lake Champlain Specimen", "medium": "Ink &amp; Watercolour", "date": "May 22, 2002", "badge": "", "color": "#667788", "desc": "A scientific illustration of the Lake Champlain monster Champ, depicted as a surviving plesiosaur. Cross-section views of the neck vertebrae, flipper structure, and hypothesized diet. Includes a 'photograph' (actually a tiny watercolour) of the famous 1977 Mansi photo."},
            {"slug": "pine-dover-demon", "title": "Cryptid Field Guide: Dover Demon", "medium": "Ink", "date": "Apr 3, 2002", "badge": "", "color": "#aabb99", "desc": "A disturbing ink illustration of the Dover Demon as reported in 1977 Massachusetts sightings. The enormous head, glowing orange eyes, and spindly body rendered with clinical precision. Witness testimony excerpts handwritten around the border."},
        ],
    },
    {
        "slug": "loch-lorna",
        "name": "Loch Lorna",
        "location": "Inverness, Scotland, UK",
        "member_since": "September 1999",
        "media": "Watercolour, Gouache",
        "influences": "Scottish landscape tradition, marine biology illustration, sonar imagery, medieval sea monster maps",
        "bio": "I live on the shores of Loch Ness (yes, really) and I paint lake monsters and sea serpents from folklore around the world. My neighbours think I'm daft, but when you've grown up watching the loch every single day, you start to see shapes in the water that don't match any fish in the book. My art imagines what lies beneath the surface of the world's most mysterious bodies of water.",
        "total_images": 13,
        "total_comments": 72,
        "gallery_created": "September 3, 1999",
        "last_updated": "July 5, 2002",
        "artworks": [
            {"slug": "lorna-nessie-deep", "title": "Nessie in the Deep", "medium": "Watercolour &amp; Gouache", "date": "Jul 5, 2002", "badge": "UPDATED!", "color": "#2a4455", "desc": "A breathtaking underwater view of the Loch Ness Monster gliding through the dark peat-stained waters of the loch. Shafts of pale Scottish light filter down from above, illuminating a long-necked plesiosaur-like creature among submerged logs and ancient stone."},
            {"slug": "lorna-ogopogo", "title": "Ogopogo at Twilight", "medium": "Watercolour", "date": "Jun 12, 2002", "badge": "", "color": "#445566", "desc": "The serpentine form of Ogopogo breaking the surface of Okanagan Lake at dusk, multiple humps visible in a line across the glassy water. The surrounding mountains are reflected perfectly, disturbed only by the creature's wake."},
            {"slug": "lorna-kraken", "title": "The Kraken Stirs", "medium": "Gouache", "date": "May 1, 2002", "badge": "", "color": "#334455", "desc": "A massive kraken rising from the abyss beneath a tiny fishing vessel off the Norwegian coast. Tentacles the width of tree trunks curl around the hull. The scale is terrifying &mdash; most of the creature is still hidden in the black water below."},
        ],
    },
    {
        "slug": "chupacabra-charlie",
        "name": "Chupacabra Charlie",
        "location": "Laredo, Texas, USA",
        "member_since": "June 2001",
        "media": "Acrylic, Spray Paint, Digital",
        "influences": "Mexican muralism, Chicano art, lucha libre poster design, borderlands folklore",
        "bio": "Yo soy Chupacabra Charlie and I paint the monsters of the borderlands! My art mixes traditional Mexican mural style with cryptid folklore from both sides of the Rio Grande. The Chupacabra, La Llorona, the Lechuza, the Donkey Lady of San Antonio &mdash; these are the creatures my abuela warned me about, and now I make them beautiful and terrifying in paint. Viva los monstruos!",
        "total_images": 10,
        "total_comments": 63,
        "gallery_created": "June 6, 2001",
        "last_updated": "July 12, 2002",
        "artworks": [
            {"slug": "charlie-chupacabra-hunt", "title": "El Chupacabra Hunts", "medium": "Acrylic &amp; Spray Paint", "date": "Jul 12, 2002", "badge": "NEW!", "color": "#883322", "desc": "A terrifying Chupacabra rendered in bold mural style, crouching on a moonlit ranch fence in South Texas. Spines bristle along its back, alien eyes glow green, and long fangs drip in the starlight. A frightened goat bleats in the background. Bold outlines and saturated colour."},
            {"slug": "charlie-lechuza", "title": "La Lechuza", "medium": "Acrylic", "date": "Jun 20, 2002", "badge": "", "color": "#332244", "desc": "A massive owl with the face of a woman perched on a power line above a lonely Texas highway at night. La Lechuza, the witch-owl of Mexican-American folklore, her wingspan blocking out the stars. A lone car's headlights approach in the distance."},
            {"slug": "charlie-donkey-lady", "title": "The Donkey Lady Bridge", "medium": "Spray Paint &amp; Acrylic", "date": "May 8, 2002", "badge": "", "color": "#554422", "desc": "A haunting figure with a distorted, elongated face stands on the old stone bridge south of San Antonio. The Donkey Lady, a local Texas legend, rendered in the gritty style of street muralism with lucha libre poster flair. The Medina River churns below."},
        ],
    },
    {
        "slug": "skunkape-shelly",
        "name": "Skunkape Shelly",
        "location": "Ochopee, Florida, USA",
        "member_since": "November 2001",
        "media": "Digital, Coloured Pencil",
        "influences": "Florida wildlife illustration, swamp ecology, Southern Gothic fiction, vintage roadside attraction signs",
        "bio": "I illustrate the cryptids of the American Southeast with a focus on Florida's weirdest. The Skunk Ape, the Pascagoula aliens, Lizard Man of Scape Ore Swamp, the Altamaha-ha &mdash; the South is crawling with creatures that don't show up in any field guide. I draw them all in a style that's half scientific illustration, half vintage Florida postcard. My studio is a screened-in porch in the Everglades and I am NOT making that up.",
        "total_images": 8,
        "total_comments": 42,
        "gallery_created": "November 15, 2001",
        "last_updated": "July 2, 2002",
        "artworks": [
            {"slug": "shelly-skunkape", "title": "Skunk Ape in the Cypress Swamp", "medium": "Digital &amp; Coloured Pencil", "date": "Jul 2, 2002", "badge": "", "color": "#445533", "desc": "Florida's own Bigfoot cousin &mdash; the foul-smelling Skunk Ape &mdash; wading through a cypress swamp at dawn. Spanish moss hangs from ancient trees, an alligator watches from a nearby bank, and the creature's matted orange-brown fur is rendered in incredible texture detail."},
            {"slug": "shelly-lizardman", "title": "Lizard Man of Scape Ore Swamp", "medium": "Coloured Pencil", "date": "Jun 10, 2002", "badge": "", "color": "#336633", "desc": "A seven-foot bipedal lizard creature with glowing red eyes standing in a South Carolina swamp at night, exactly as described by witnesses near Bishopville in 1988. Green scales, three-fingered claws, and a muscular tail. Drawn in hyper-detailed coloured pencil."},
            {"slug": "shelly-altamaha", "title": "The Altamaha-ha Surfaces", "medium": "Digital", "date": "May 1, 2002", "badge": "", "color": "#556644", "desc": "Georgia's own sea serpent, the Altamaha-ha, breaking the surface of the Altamaha River. A long snakelike neck, a body like a sturgeon but enormous, and a tail that churns the muddy water for twenty feet. Painted in the warm golden light of a Georgia sunset."},
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
