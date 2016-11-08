# Rpic Rpg
#### Mission Statement:
I want to create a fully dynamic RPG AI and Event scripting library. I chose python to do this since it has broad support and diverse package availability, however a fair enough argument for another technology will be entertained. My goal is to be able to create an entire RPG world filled with dynamic everything, including Locations, Buildings, Items, NPCs, Factions, Knowledge Systems, Quest Systems as well as supporting raw-text input from the user and more. Ask anyone about anything you can think of. Even ask key NPCs about endgame events before they happen (with consequences).

# Core Ideas

#### Raw-Text Input
User interactions will be raw-text based, so the user will have access to their keyboard to talk to the game. The system will take user input and fuzzy-match against a collection of possible inputs and ask the user which one they intended, with the option to add something new.

#### Text positivity
Using the python `textblob` library, we are able to calculate the positivity of a phrase based on the words used. This positivity value can influence how the world reacts to players choices.

#### NPC AI
NPCs will be able to learn from the player and discuss amongst themselves. When a player says something to an NPC, the positivity of the text will be analyzed and will influence the NPC's demeanor towards the player. NPC's will have a dynamic list of locations that they visit, and when two NPCs of the same faction meet up, there will be a chance of them discussing what the player previously told them.

### I need help though!
I am not a game developer. I do have 7 years of rather diverse programming experience under my belt, plus I've been playing RPGs since I was a wee lad when my dad brought home an NES and the first Legend of Zelda. I've spent countless hours in Ultima IV and Morrowind enjoying the content and dreaming of ways it could be even better. I've had quite a few ideas for this, and I am trying to accumulate them here. I need **YOUR** help to discuss what should be added or removed, how things should interact, implementation details, etc. No idea is too small to share, so if you get one, *please* create an issue on this repository and we can discuss it.

## Contributing
Since the project is still extremely young, most contribution efforts should be focused on adding text-content such as:
* Text Template **FOR ALL MESSAGES**
  * `(positivityRating, text, context)`
    * E.x.: (10, "Yes most definitely!", [1,2])
    * E.x.: (1, "Oh hell no.", [1])
  * PositivityRating: is a value between 1-10 which identifies how positive a statement is.
  * Text: is the string value for the message.
  * Context: varies depending on interaction type;

* NPC's
  * NPC Welcome Messages - I just interacted with an NPC, what does he say?
  * NPC Idle Messages - What I hear in a crowd of NPC's
  * NPC Radius Messages - I've been standing near this NPC for more than a few seconds, he asks what i'm doing or something.
  * Text Template Context:

      | ID  | Description |
      | --- | ----------- |
      | `1` | Direct Interaction with NPC |
      | `2` | Walking past/overheard with NPC |
      | `3` | In response to world-event |

* Player Text *"Where am I?"* or *"Oh, what's this?"*
  * Initial Interaction - NPCs
  * Initial Interaction - Creatures
  * Initial Interaction - World Items
  * Initial Interaction - Inventory Items
  * Text Template Context:

      | ID  | Description |
      | --- | ----------- |
      | `1` | Direct Interaction with NPC |
      | `2` | Creature Interaction |
      | `3` | World Item Interaction |
      | `4` | Bag Item Interaction |
      | `5` | World Object Interaction |

* Quests
  * EventChain Messaging
    1. Trigger (how the quest starts) *(player says something about dogs, and gets asked about quest to find lost dog)*
    2. NPC quest initialize dialog
    3. Text options available at each stage of the quest.
    4. Offering Faction (if applicable) *which group to turn the quest in to*
    5. Tiered quest rewards *based on time to completion, questy path taken, etc*.

