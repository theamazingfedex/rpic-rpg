# pylint: disable=C0321
# pylint: disable=W0141
# pylint: disable=C0103
"""Better Game World - NPC interaction choices"""

# (positivity, phrase, context)
#   Context:
#     1. Direct Interaction
#     2. Walking past/overheard
#     3. In response to world-event
introductions = [
    (10, "Yes?", [1, 2]),
    (4, "What do you want?", [1, 2]),
    (10, "How can I help you?", [1, 2])
    ]

# Fuzzy match raw input against these
# (positivity, phrase, context)
#   Context:
#     1. NPC Interaction
#     2. Creature Interaction
#     3. Item Interaction
#     4. World Interaction
player_options_standard = [
    (7, "Where am I?", [1]),
    (6, "Who are you?", [1, 2]),
    (5, "What can you tell me about the area?", [1, 2, 3]),
    (4, "What is your story?", [1, 2]),
    (8, "Have you anything for sale?", [1])
    ]

# Fuzzy match raw input against these
player_options_global = [
    (),
    (),
    ()
    ]

quests_global = [
    (),
    (),
    ()
    ]

quests_region_01 = [
    (),
    (),
    ()
    ]
