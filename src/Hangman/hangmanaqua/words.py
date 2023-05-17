import levels

# 4 letter words / level 1
four_letter_words = ["acid", "blog", "clay", "dead", "envy", "firm", "glue", "haul", "inch", "jazz", "king", "lawn", "melt", "nova", "okay", "pool", "rage", "sack" , "turf", "user", "vein", "ward", "yarn", "zoom"]

# 5 letter words / level 2
five_letter_words = ["abuse", "abbey", "badly", "beast", "boost", "carol", "cease", "dried", "elbow", "forge", "judge", "lease", "magic", "mason", "outer", "prime", "shelf", "swept", "sweet", "trout", "urban", "vapor", "worse", "youth", "yacht"]

# 6 letter words / level 3
six_letter_words = ["active", "ballet", "cancel", "debris", "escape", "frozen", "golden", "hazard", "honest", "intend", "kidney", "linear", "luxury", "nephew", "plasma", "ritual", "throat", "upward", "verify", "vision", "wooden", "worthy", "yearly", "yellow"]

# FIXME: 7 letter words / level 4
seven_letter_words = []

# FIXME: 8 letter words / level 5
eight_letter_words = []

def level_words():
    if levels.level == 1:
        return four_letter_words
    elif levels.level == 2:
        return five_letter_words
    elif levels.level == 3:
        return six_letter_words
    elif levels.level == 4:
        return seven_letter_words
    return eight_letter_words

# #7 letter words/level 4
# abandon
# absence
# beloved
# bicycle
# century
# carrier
# defense
# deposit
# evening
# ethical
# fishing
# finance
# grammar
# gradual
# immense
# imagery
# lateral
# landing
# lawsuit
# married
# mandate
# nuclear
# paradox
# retired
# stadium

# # 8 letter words/level 5
# aviation
# birthday
# colorful
# customer
# dialogue
# envelope
# exchange
# firewall
# generate
# graphics
# interior
# judgment
# lifetime
# location
# modeling
# negative
# official
# painting
# princess
# recovery
# sampling
# slightly
# together
# umbrella
# violence
