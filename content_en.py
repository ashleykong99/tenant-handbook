# -*- coding: utf-8 -*-
"""English tenant handbook content data."""

def V(i, label): return {"type": "video", "id": i, "label": label}
def P(i, cover, label): return {"type": "pdf", "id": i, "cover": cover, "label": label}
def D(i, label): return {"type": "doc", "id": i, "label": label}
def L(i, label): return {"type": "link", "id": i, "label": label}
def IMG(src, label): return {"type": "image", "src": src, "label": label}

CATEGORIES = [
{
  "id": "notice",
  "emoji": "📋",
  "title": "Move-in Guide",
  "desc": "Front desk, access, parcels, facilities, moving, waste",
  "questions": [
    {
      "q": "Building Front Desk & Key Contacts",
      "blocks": [
        {"t": "The building front desk is open 24/7, all year round:"},
        {"list": [
          "Concierge: daily 7:00am–11:00pm",
          "Security: daily 11:00pm–7:00am",
          "Building Manager's Office: Mon–Fri 9:00am–5:00pm",
          "Urgent matters: contact the front desk first; they will escalate to building management",
        ]},
        {"h": "Key Contacts"},
        {"table": {
          "header": ["Contact / Department", "Details"],
          "rows": [
            ["Operations Manager – Pauline Tan", "0456 436 159 / pauline.tan@focusedfm.com.au"],
            ["Building Manager", "0467 888 058 / AuroraBM@focusedfm.com.au"],
            ["Assistant Building Manager – Ans Alvi", "0448 149 772 / auroraassistantbm@focusedfm.com.au"],
            ["Concierge / Security", "0497 777 057 / auroraconcierge@focusedfm.com.au"],
            ["Focused Facilities Management", "(03) 9329 4016 / info@focusedfm.com.au"],
          ],
        }},
      ],
    },
    {
      "q": "WeWumbo App Registration",
      "blocks": [
        {"t": "All residents must register on the WeWumbo App for:"},
        {"list": [
          "Identity verification",
          "Facility and moving-lift bookings",
          "Parcel notifications",
          "Building announcements",
          "Other building service requests",
        ]},
        {"h": "When registering"},
        {"list": [
          "Select Tenant or Owner",
          "New residents select 【Moving In】; existing residents select 【Existing】",
          "Select your zone: Stratus (Levels 10–30) / Cumulus (Levels 32–60) / Australis (Levels 63–85)",
          "Upload a valid photo ID",
          "Tenants upload their Lease Agreement",
        ]},
      ],
    },
    {
      "q": "Moving In & Moving Out",
      "blocks": [
        {"h": "Booking Requirements"},
        {"list": [
          "Must book via WeWumbo: Move in/out Lift & Loading Dock",
          "At least 8 hours in advance",
          "Without a booking, the building may refuse the move",
          "Confirm the lift time slot before booking your removalist",
        ]},
        {"h": "Allowed Moving Times"},
        {"list": [
          "Mon–Sat: 9:00am–5:30pm",
          "Sunday & public holidays: moving not allowed",
          "Each booking: up to 3 hours",
        ]},
        {"h": "Moving Lifts"},
        {"table": {
          "header": ["Levels", "Lift", "Internal Dimensions", "Door Opening"],
          "rows": [
            ["10–60", "Lift C", "1800L × 2100W × 2600H mm", "1300W × 2100H mm"],
            ["63–85", "Lift G", "1400L × 2000W × 2700H mm", "1100W × 2100H mm"],
          ],
        }},
        {"t": "Dimensions exclude lift protective padding; allow extra margin for furniture."},
        {"h": "On Moving Day"},
        {"list": [
          "Removal trucks enter the Loading Dock via Little La Trobe Street",
          "The resident and removalist must register at the Concierge first",
          "Collect the relevant keys and moving route instructions",
          "Notify the Concierge and return the keys when finished",
          "All luggage and packing waste must be removed by the resident or removalist",
          "The resident is liable for damage to the Loading Dock, lifts, lobbies and corridors",
        ]},
        {"t": "If the rules are not followed, the building may refuse the move and is not liable for removalist cancellation, waiting or other costs."},
      ],
    },
    {
      "q": "Access, Keys & Intercom",
      "blocks": [
        {"h": "Intercom"},
        {"t": "When a visitor enters your apartment number and rings:"},
        {"list": [
          "Press Answer to pick up",
          "Press 【Door Release & Lift Release】 to: unlock the entry door for ~5 seconds, and enable lift access for ~180 seconds",
          "The lift will only allow the visitor to select your floor",
        ]},
        {"h": "Keys & Access"},
        {"list": [
          "Apartment Key: enters your apartment",
          "FOB: enters the building, lifts and facility areas",
          "Car Park Remote: opens the car park roller door",
        ]},
        {"h": "Note"},
        {"list": [
          "If you are locked out, contact your agent",
        ]},
      ],
    },
    {
      "q": "Parcels & Food Delivery",
      "blocks": [
        {"h": "Delivery Address Format"},
        {"t": "Must include:"},
        {"list": [
          "Recipient's full name",
          "Mobile number",
          "Full address, e.g.: 8601/228 La Trobe Street, Melbourne VIC 3000",
        ]},
        {"t": "Incomplete details may cause delivery delays or loss."},
        {"h": "Small Parcels"},
        {"list": [
          "Usually placed in your mailbox by the courier",
          "Not always notified — check your mailbox regularly",
          "Tenants who lose their mailbox key should contact us; owners can contact the front desk",
        ]},
        {"h": "Medium Parcels"},
        {"list": [
          "Registered by the front desk on WeWumbo",
          "You receive a collection notification via the App",
          "You must be registered on WeWumbo to receive notifications",
          "Uncollected after 28 days — returned to sender",
        ]},
        {"h": "Large Parcels (front desk only accepts within these limits)"},
        {"list": [
          "No more than 15kg",
          "No larger than 550mm × 300mm × 300mm",
          "Must be collected within 3 days of receiving the SMS",
          "Overdue parcels are returned to sender",
        ]},
        {"h": "Furniture, appliances etc. exceeding the limits"},
        {"list": [
          "The front desk can help contact you, but you must collect immediately at the Loading Dock",
          "Multiple large items may require a moving-lift booking",
          "The front desk may refuse if you cannot collect in time",
          "Notify the front desk in advance when signing; oversized items still need someone else to receive them",
        ]},
        {"h": "Important Disclaimer"},
        {"list": [
          "The building management is not responsible for loss, damage or theft of parcels after they are handed to the front desk",
          "Valuables should be received in person wherever possible",
        ]},
        {"h": "Food Delivery"},
        {"list": [
          "The front desk does not accept food, takeaway or fresh groceries",
          "Track your delivery and collect it in the lobby in person",
          "The building is not responsible for spoilage or loss from late collection",
        ]},
      ],
    },
    {
      "q": "Noise Restrictions",
      "blocks": [
        {"t": "Residential noise is prohibited during these times:"},
        {"table": {
          "header": ["Day", "Restricted Hours"],
          "rows": [
            ["Mon–Thu", "Before 7:00am, after 10:00pm"],
            ["Friday", "Before 7:00am, after 11:00pm"],
            ["Saturday & public holidays", "Before 9:00am, after 11:00pm"],
            ["Sunday", "Before 9:00am, after 10:00pm"],
          ],
        }},
        {"t": "Even outside these hours, prolonged or excessive noise may still be unreasonable."},
        {"h": "If You Experience Noise"},
        {"list": [
          "Contact the Concierge or Security immediately",
          "Record the time, noise type, and audio/video where possible",
          "The front desk or security will investigate and give a verbal warning",
          "Persistent issues escalate to the Owners Corporation",
          "Serious or ongoing noise can be reported to police",
        ]},
      ],
    },
    {
      "q": "Smoking & Common Areas",
      "blocks": [
        {"h": "No Smoking / No Vaping"},
        {"t": "Smoking or vaping is strictly prohibited in these common areas:"},
        {"list": [
          "Corridors",
          "Lobby and lift lobbies",
          "Car park and basement areas",
          "Fire stairs",
        ]},
        {"t": "Violations may trigger the fire alarm and a Breach Notice."},
        {"t": "If cooking or smoking inside your apartment:"},
        {"list": [
          "Do not open the entry door to ventilate",
          "Open the windows instead",
          "Smoke entering the common corridors may trigger the building fire alarm",
        ]},
        {"h": "Common Areas"},
        {"list": [
          "No littering",
          "No doormats, shoes or personal items",
          "Fire escape routes must stay clear",
          "Common-area power outlets are for building maintenance only",
          "Not for private use or EV charging",
          "Violations will receive a Breach Notice",
        ]},
      ],
    },
    {
      "q": "Facilities & Opening Hours",
      "blocks": [
        {"t": "Facilities available depend on your floor:"},
        {"table": {
          "header": ["Resident Zone", "Facility Levels"],
          "rows": [
            ["Stratus 10–30", "Level 8"],
            ["Cumulus 32–60", "Levels 8 & 61"],
            ["Australis 63–85", "Levels 8, 61 & 86"],
          ],
        }},
        {"t": "All facilities that require booking must be approved via WeWumbo."},
        {"h": "Key Facilities"},
        {"list": [
          "Level 8: gym, 25m pool, steam room, sauna, yoga room, kitchen, BBQ area",
          "Level 61: lounge, wine cellar, games lounge, meeting rooms, dining room, karaoke room",
          "Level 86: Australis Lounge, kitchen, dining room, Moonlight Cinema, gym, yoga room, reading lounge",
        ]},
        {"h": "Key Opening Hours"},
        {"list": [
          "Gym & yoga room: 24 hours",
          "Pool, steam room & sauna: 6:00am–10:00pm",
          "Most lounges & function rooms: 8:00am–11:00pm",
          "BBQ area: 9:00am–11:00pm",
        ]},
      ],
    },
    {
      "q": "Facility Use Rules",
      "blocks": [
        {"h": "Usage Rules"},
        {"list": [
          "For residents and their invited guests only",
          "No selling, booking for others, or external renting",
          "The booking resident must be present at all times",
          "Register and sign the confirmation form at the Concierge before use",
          "One company may only book the same room once per day",
          "No consecutive bookings",
          "Each facility may be booked up to 5 times per month",
          "Under-16s must be accompanied by an adult",
          "Clean up and dispose of rubbish after use",
          "Residents are responsible for their guests' behaviour",
          "The booking resident pays for any damage",
          "No decorations fixed to walls, doors or other surfaces",
          "Turn off power, gas, air conditioning and lights before leaving",
          "No photography or recording in the gym, pool, sauna, steam room or yoga room without permission",
        ]},
        {"h": "Prohibited in Function Rooms"},
        {"list": [
          "Excessive alcohol",
          "Smoking or vaping",
          "Pets",
          "Amplified music",
          "Glass and fragile items",
          "Sharp objects",
          "Private appliances or kitchen equipment",
        ]},
        {"h": "Pool, Steam Room & Sauna"},
        {"list": [
          "Pool size: 25m long, 5m wide, 1.2m deep",
          "Shower before entering the pool",
          "No diving, running or dangerous play",
          "Bring your own towel",
          "Dry off before leaving the pool area",
          "Wet clothes and shoes must not be taken outside the pool area",
          "No skinny-dipping",
        ]},
        {"t": "Pregnant women, or people with heart, circulatory, respiratory, blood pressure, diabetes, kidney or other conditions, are not advised to use the steam room or sauna. Also wait until you have recovered after drinking, eating or exercising."},
      ],
    },
    {
      "q": "Waste Disposal",
      "blocks": [
        {"t": "At the time of publishing, the garbage chute is temporarily out of use. Current requirements:"},
        {"list": [
          "Do not leave rubbish in the bin room, chute or floor common areas",
          "General waste and recyclables must go to B1",
          "Tie rubbish securely and double-bag it to prevent liquid staining the carpet",
          "Large cardboard boxes must be flattened",
          "Do not put furniture, appliances or bulky items in general bins",
          "N2O (nangs/laughing gas) canisters must not go in general, recycling or bulky waste — contact the supplier",
          "Do not leave rubbish on the ground",
        ]},
        {"h": "Lifts to B1"},
        {"list": [
          "Lift C: lower and mid-rise residents",
          "Lift G: high-rise residents",
        ]},
        {"t": "On weekdays 9:00am–6:00pm, Lifts C and G may be locked for moving bookings, so dispose of waste 【weekdays 6:00pm–9:00am next day】; Sundays and public holidays are usually available all day."},
        {"h": "Bulky Waste"},
        {"list": [
          "Collected on the first Saturday of each month",
          "Only place items in the B1 designated area on the collection date",
        ]},
        {"h": "E-waste"},
        {"list": [
          "Place in the E-waste Bin near the bulky waste area",
          "Electrical items only",
          "No general waste, cardboard or non-electronic bulky items",
        ]},
        {"h": "Donation Bin"},
        {"list": [
          "Placed at the Loading Dock every second Friday",
          "Collected on Saturday",
          "Clothing and apparel only",
          "No furniture or appliances",
        ]},
      ],
    },
  ],
},
{
  "id": "inspection",
  "emoji": "🔍",
  "title": "Move-in Inspection",
  "desc": "Furniture, cleaning, replacing furniture",
  "questions": [
    {
      "q": "There are small furniture/items I don't want — what do I do?",
      "blocks": [
        {"t": "Tell your Property Manager what you don't want and ask for a copy of the 【Original Property Report】. This report records the property's condition before the landlord rented it out. Any furniture/items 【not recorded】 are mostly left by previous tenants, and you may dispose of them yourself (normally bulky items go to the apartment hard-rubbish collection with a booked moving lift — best to check with the Building Manager or front desk first; the PM is not responsible for this). Note: if there are special cases like furniture replacement or new landlord-supplied furniture, we will inform you separately."},
      ],
    },
    {
      "q": "The apartment feels dirty — can the landlord/previous tenant reimburse cleaning or arrange a re-clean?",
      "blocks": [
        {"t": "All apartments are professionally cleaned + carpet steam-cleaned before keys are handed over. You can ask your Property Manager for a cleaning receipt as proof."},
        {"t": "Note that everyone's cleaning standard differs, and we have inspected and passed the apartment against our standard. Possible situations: carpets shed a lot of dust (wool carpets naturally shed a lot of fibre), opening windows or wearing shoes indoors causes dust/hair, and mattress sweat stains are hard to avoid — you may bring your own mattress protector if concerned. For obvious benchtop grease or large mattress stains, we will arrange a cleaning re-do."},
      ],
    },
    {
      "q": "Can I replace a mattress / sofa / other furniture?",
      "blocks": [
        {"t": "We understand everyone has their own furniture preferences. If you strongly want to replace something, first find a product of 【similar style and price】 and send it to your Property Manager for approval. Once approved, arrange disposal yourself (as above) and arrange the new furniture to come in (remember to coordinate lift booking with the Building Manager or front desk — the PM is not responsible for this)."},
      ],
    },
  ],
},
{
  "id": "maintenance",
  "emoji": "🔧",
  "title": "Maintenance",
  "desc": "Door locks, appliances, plumbing & electrical",
  "note": "Before reporting maintenance: make sure you have read this handbook and followed the instructions. If it still doesn't work, take photos and videos and send them to Protique-leasing on WeChat / WhatsApp 0422329166",
  "questions": [
    {
      "q": "Something is broken — how do I report it?",
      "blocks": [
        {"t": "If discovered just after moving in, we may already be aware of it and are negotiating with the previous tenant or waiting for a tradesperson. If discovered later (after 5 working days), report it to the PM with 【photos and videos】. Non-urgent repairs are completed within the legal 14 days; urgent repairs are aimed to be done within two days (urgent vs non-urgent depends on 【whether minimum rental standards are affected】, including but not limited to leaks, explosions, cooktop completely unusable, toilet completely unusable, unable to shower, etc. — search online for details). As Australian labour is expensive and some repairs need tenant cooperation for initial checks, common issues are listed below."},
      ],
    },
    {
      "q": "How do I change the digital door lock?",
      "blocks": [
        {"t": "Open the door with the key first, and with the 【door open】, follow the video and file below step by step. The initial password is 【1234#】."},
        {"media": [
          V("10q6Lu4rwoRRwhxUf3HQlqSS0yU2d8T1F", "Digital lock setup video"),
          P("19ld0-78T3KH2O7qqolz6wZoATfWT8N5C", "assets/cover-samsung-lock.png", "Samsung Digital Locking Form"),
        ]},
      ],
    },
    {
      "q": "A light isn't working — what do I do?",
      "blocks": [
        {"t": "Two cases. First, an electrical circuit problem — we send an electrician, paid by the landlord. Second, just a blown bulb — a tenant usage issue. We can help arrange a tradesperson; minimum call-out $80+GST, or $40+GST per bulb if combined with other items — this cost is borne by the tenant. You can also replace it yourself:"},
        {"media": [
          V("15hbjoq_0KgoOCE3WKCJICMTqDTT0JprM", "Downlight change video"),
        ]},
      ],
    },
    {
      "q": "A window won't open / won't stay open?",
      "blocks": [
        {"t": "Tighten the screws shown in the image below. If it still doesn't work, ask the building front desk — they can help repair it."},
        {"media": [
          IMG("assets/img-window.jpg", "Window screw location"),
        ]},
      ],
    },
    {
      "q": "The fridge isn't working — what do I do?",
      "blocks": [
        {"t": "Two cases. First, the fridge hums but doesn't cool properly — if it has a power switch, long-press it; otherwise turn the breaker off and on. Second, the fridge doesn't cool/freeze — most commonly the air duct or outlet is blocked by ice. Most fridges are single-evaporator with a fan circulating cold air; if the evaporator frosts up or the duct freezes, it stops cooling."},
        {"t": "Solution: first 【power off completely for 24–36 hours with the door open to let the ice fully melt】 (unplug if possible; if built-in and can't unplug, turn off the breaker), then dry the inside and power back on to test."},
        {"t": "If the freezer frosts up heavily, the drain may be blocked — try cleaning it:"},
        {"media": [
          V("1g6WxgFTSYjQL9rfoyLt0owcR902clmMc", "Fridge drain clearing video"),
        ]},
        {"t": "If it doesn't recover, contact the PM and we'll arrange repair/replacement."},
      ],
    },
    {
      "q": "The cooktop / induction cooktop isn't working?",
      "blocks": [
        {"t": "For induction, first check power under the cabinet. For gas cooktops (after confirming power and gas), two cases: first, the flame goes out when you release the knob — get a piece of 【sandpaper】 from the office and sand the small white pin to restore the flame. Second, you only hear a 'hissing' sound with a tiny flame — the exhaust port is blocked; get a 【simmer needle】 from the office to clear it. These are tenant usage issues — clean the cooktop after cooking, don't let oil seep into the gas stove, and don't use alcohol-based cleaners."},
        {"media": [
          IMG("assets/img-cooktop-no-fire.jpg", "Cooktop no-fire guide"),
          V("1TfzbCQej1cJsEDMsJCqvTVEDzqxWi2C-", "Cooktop video 1"),
          V("1p5qEv5h_UjQKJ4s93oi_wvxZEe9pZU6J", "Cooktop video 2"),
          V("1yOCBIX8n1i8qzBpzsAVF3z7-wXl7zOuj", "Gas stove igniter not working"),
        ]},
        {"t": "If these don't resolve it, contact the PM."},
      ],
    },
    {
      "q": "The oven light isn't working?",
      "blocks": [
        {"t": "A non-working light doesn't affect use. If the oven itself is unusable, it will be noted before you move in."},
      ],
    },
    {
      "q": "The dishwasher isn't working — what do I do?",
      "blocks": [
        {"t": "First check power under the cabinet; the screen will show an error code. Search the error code + model + brand online for solutions. The most common issue is a blocked outlet causing no draining — remove and clean the hose cover and filter, and long-press the power button for 15 seconds to restart. These are tenant usage issues."},
        {"media": [
          V("12jejWAY8s244tBrLs312Jz1FsPUOPVoG", "Miele dishwasher cleaning"),
          V("1ZgCpZpMIQ81oaO9S1OPsiaf_rjucRzWT", "Miele upper rack adjustment"),
          V("1-YJOd2ElwhrLuucDoVVnZKmg6Sk0BdyZ", "Fisher & Paykel cleaning"),
          D("1A0CVc8c2OmZiQ_5wCKFCgSl3vcqO_RKaSXbunuWIoSE", "Fisher & Paykel not draining"),
          V("164lrzpDHoRzS9UkwIlzo3k6y0z7_vmUt", "Upper water supply hose dropped"),
          D("1qEuq0doK2qSCWKhv3YhA158wyZvyxaFPITm1IaIOpJs", "Dishwasher cleaner"),
        ]},
        {"t": "If it still doesn't work, contact the PM."},
      ],
    },
    {
      "q": "The washing machine isn't working?",
      "blocks": [
        {"t": "First check power/switch; the screen will show an error code — search error code + model + brand online. Try restarting first: turn off, unplug, wait 5–10 minutes, plug back in. Won't start → check the door is fully closed; won't spin → check if the load is too heavy or on one side; won't drain → check the filter is blocked (small door near the bottom) or the drain hose is blocked. These are tenant usage issues."},
        {"media": [
          IMG("assets/img-laundry.jpg", "Laundry room diagram"),
          V("1gZ7EuWBbN5ZPP2b9ErOBNnLFzwRzMx0t", "Washing machine cleaning"),
          V("1ASLRslNYOCZ8NmpeFTQgoWc6W99qRb89", "No power? Troubleshooting"),
          V("1uo4m5SFIa1A0-8qp9tQuzNoE7i6zMwFM", "U-bend installation"),
          V("1qfqrjvO1rZsWNLQnXrzBw34b2DysZdLg", "Draining / filter cleaning"),
          V("1z7tjaUOePG0p2BEZ7dPLqEYn8AXrSnb3", "Door seal gap"),
        ]},
        {"t": "If it still doesn't work, contact the PM."},
      ],
    },
    {
      "q": "The dryer isn't working?",
      "blocks": [
        {"t": "First check power/switch; the screen will show an error code. Try restarting: turn off, unplug, wait 5–10 minutes. Won't start → check the door is closed; won't dry → check the load is too heavy or the water tank is full (pull out the drawer near the top); won't drain → check the filter is blocked (bottom or side of the door seal), remove and clean the lint. These are tenant usage issues. If it still doesn't work, contact the PM."},
        {"media": [
          P("1wpSqOSXvgzWKwaHOw7JQvMDw7t53Q5yI", "assets/cover-miele-dryer-06086650.png", "Miele dryer manual"),
          P("1yHWQ7s48-vQaUrQoS9z35WNJctMElNQW", "assets/cover-miele-dryer-manual.png", "Miele dryer user manual (English)"),
        ]},
      ],
    },
    {
      "q": "The basin won't drain?",
      "blocks": [
        {"t": "Usually hair is tangled/blocking it — a tenant usage issue; never wash your hair in the basin! Buy a bottle of Drano (the large orange bottle):"},
        {"media": [
          P("1eS0Tf8Zw1bi0DwT9hVaC0IhK2RSoplzX", "assets/cover-drainage.png", "Drain blockage guide"),
        ]},
        {"t": "Pour half a bottle into the dry basin, wait 12 hours, then flush with hot water for a few minutes. If it still doesn't work, contact the PM."},
      ],
    },
    {
      "q": "The toilet is leaking / won't flush?",
      "blocks": [
        {"t": "First open the cistern lid and turn off the water valve to stop further leaking, then contact the PM."},
      ],
    },
    {
      "q": "Toilet seat misaligned?",
      "blocks": [
        {"media": [
          V("1ugDYpdDQ_6Jl0Q5IOWOJOHvo2kB2mkzM", "Toilet lid removal"),
          V("1Lho8xOBrzWpeMKdEt-iSOO9xMYGBbhNc", "Toilet repair guide"),
          V("14Cd9tVAQ3oTwm0lyQl7L0AUiqYXjisBk", "Loose toilet seat"),
        ]},
      ],
    },
    {
      "q": "Tap fell off? / Basin button won't pop up?",
      "blocks": [
        {"media": [
          V("1RSAiAElSkCmBzKP2U3M28KjO7JIx6u9a", "Tap repair"),
          V("1iNE2jtgXa6JO76-Mw5oDUHaFR5uqeSua", "Basin button stuck"),
        ]},
      ],
    },
    {
      "q": "The air conditioner isn't working?",
      "blocks": [
        {"t": "If the panel shows an error code, contact the front desk to restart the main unit. Clean the filter if needed:"},
        {"media": [
          V("1ndRNfxaL47Gd6fEthOzQwarDRC_TQTo_", "AC filter removal & cleaning"),
        ]},
      ],
    },
    {
      "q": "The bed frame has collapsed?",
      "blocks": [
        {"t": "Follow the repair video below:"},
        {"media": [
          V("1ImyJ3kPlclJmEN_Th_kA8Ak_9-yrZKEc", "Bed frame repair"),
        ]},
        {"t": "If it still doesn't work, contact the PM."},
      ],
    },
    {
      "q": "Smoke alarm not working / constantly beeping?",
      "blocks": [
        {"t": "It may need a new battery or a reset:"},
        {"media": [
          V("1I8andRHgm7oWRm0-QtjHyHwVUzXwA3U0", "Smoke alarm battery change"),
          V("1WDC561s9S8fji2_azyYb-Ow8EGZnbgtv", "Resetting a beeping smoke alarm"),
        ]},
      ],
    },
  ],
},
{
  "id": "emergency",
  "emoji": "🚨",
  "title": "Emergency",
  "desc": "Lost keys, power outage, fire, urgent contacts",
  "questions": [
    {
      "q": "I've lost my key — what do I do?",
      "blocks": [
        {"t": "First confirm whether it's the fob (the disc for the lift), the hard key (for your apartment door), or the mailbox key."},
        {"t": "If it's the fob: check the back of any remaining fob for a number, then pay two transfers: $95 to O Real Investment Trust (BSB 033002, Acc 037975), and $110 to O REAL (BSB 733003, Acc 727393). After receiving the transfer screenshot we order from the building — usually within two weeks."},
        {"t": "If the hard key is lost: it cannot be reordered — a $200 charge applies."},
        {"t": "If the mailbox key is lost: transfer $25.30 and we'll order one from a locksmith."},
      ],
    },
    {
      "q": "What to do during a power outage?",
      "blocks": [
        {"list": [
          "Check the Master Switch near the entry door is on",
          "Check the Circuit Breaker is on",
          "If it has tripped, unplug the appliance that caused it and reset",
          "If it trips again: tenants contact their agent; owners contact an electrician",
          "If switches are fine but there's still no power, contact the Origin Energy emergency hotline",
        ]},
      ],
    },
    {
      "q": "Fire & Emergency Evacuation",
      "blocks": [
        {"h": "Assembly Point"},
        {"t": "The fire evacuation assembly point is: 【State Library Victoria Forecourt】."},
        {"t": "The spiral stairs in each mid-floor lead to the fire stairs; follow the fire evacuation signage."},
        {"h": "Lower & Mid-rise Residents (Levels 10–60)"},
        {"list": [
          "Do not search for the fire source or collect belongings during a fire alarm",
          "Check the door and handle with the back of your hand before opening",
          "Use the stairwell to reach the fire stairs",
          "Do not use the lifts",
          "Follow the Fire Warden's instructions",
          "If the exit/stairwell is blocked by smoke, call the Royal Call Centre",
          "Use the emergency phone inside each floor's door if you need assistance",
          "Do not re-enter the building until permitted",
        ]},
        {"h": "High-rise Residents (Levels 63–85)"},
        {"list": [
          "During a fire, high-rise lifts may be used for evacuation if emergency instructions allow",
          "If smoke is present, use the fire stairs to the Level 61 Refuge Areas",
          "Level 61 refuge areas include: Cumulus Lounge, Games Lounge, Wine Cellar",
          "These areas have independent systems, communications and fire doors for waiting",
        ]},
      ],
    },
    {
      "q": "Preventing False Alarms",
      "blocks": [
        {"list": [
          "Don't place pots or ovens near smoke detectors, and don't block extinguishers, fire doors or sprinklers",
          "Don't cover smoke detectors",
          "When cooking produces smoke, open the windows to vent it and avoid triggering the alarm",
          "Familiarise yourself with the fire plan and evacuation routes in advance",
        ]},
        {"h": "Smoke Alarms Inside Apartments"},
        {"list": [
          "Usually on the ceiling of the hallway outside the bedroom",
          "Normally not connected to the building's active fire system",
          "They sound independently when they detect smoke (usually not controlled by the fire brigade/management)",
          "But you should attend to them promptly",
          "Do not cover or remove the detector",
        ]},
        {"h": "Common-area Sounders"},
        {"t": "Common-corridor sounders are connected to the building fire system; once triggered they automatically notify the fire brigade. So when the alarm sounds, never open your apartment door to check the cause."},
      ],
    },
    {
      "q": "Emergency & Helpline Numbers",
      "blocks": [
        {"table": {
          "header": ["Service", "Phone"],
          "rows": [
            ["Police, Fire, Ambulance (emergency)", "000"],
            ["Non-emergency police assistance", "13 14 44"],
            ["Nurse on Call", "1300 60 60 24"],
            ["Health Direct", "1800 022 222"],
            ["Lifeline (crisis support)", "13 11 14"],
            ["Victoria Legal Aid", "1300 792 387"],
          ],
        }},
      ],
    },
    {
      "q": "Weekend/public holiday urgent repairs — who do I contact?",
      "blocks": [
        {"t": "On weekends or public holidays, if you cannot reach the Property Manager and have an urgent repair (urgent cases only, e.g. water leaks, electrical faults, locked out), contact these tradespeople:"},
        {"table": {
          "header": ["Trade", "Name", "Phone"],
          "rows": [
            ["Handyman", "Alvis", "0416 971 157"],
            ["Electrical", "Wang", "0415 264 700"],
            ["Plumbing", "David", "0430 014 680"],
            ["Locksmith", "Paul", "0410 974 734"],
          ],
        }},
      ],
    },
  ],
},
{
  "id": "contract",
  "emoji": "📝",
  "title": "Contract & Subletting",
  "desc": "Renewal, roommates, subletting",
  "questions": [
    {
      "q": "My lease is expiring — can I renew?",
      "blocks": [
        {"t": "Generally, if the landlord has no special arrangements and you have kept the property in good condition (no damage, clean and tidy), you can renew for a year or six months. Ask the PM for details."},
      ],
    },
    {
      "q": "I have a new roommate — how do I add them to the lease?",
      "blocks": [
        {"t": "Yes. Send your roommate's details to the PM (passport or driver's licence, visa + COE or Medicare, bank statement or payslip, application form) for review. Once approved, we issue a new contract; there is a small fee for the name change."},
      ],
    },
    {
      "q": "Due to circumstances beyond my control I can't continue the lease — what now?",
      "blocks": [
        {"t": "You can sublet by finding a new person to take over. Subletting incurs a fee as noted in the contract; once a replacement is confirmed, the fee can be paid separately or deducted from the bond after move-out."},
        {"t": "You can advertise on social media yourself, or ask us to advertise on realestate.com and domain. The advertising fee is $330 paid upfront, to O REAL (BSB 733003, Acc 727393)."},
        {"t": "Note: paying the advertising fee does not guarantee we can find a replacement tenant. Until the contract ends, the tenant on the lease is liable for rent until it ends."},
      ],
    },
    {
      "q": "I've found someone to take over — what happens next?",
      "blocks": [
        {"t": "Send the new person's details to the PM (passport or driver's licence, visa + COE or Medicare, bank statement or payslip, application form) for review. Once approved, we arrange a new contract; after the new tenant signs and pays the bond and first month's rent, you pay the sublet fee and arrange the move-out process."},
      ],
    },
  ],
},
{
  "id": "move-out",
  "emoji": "🔑",
  "title": "Moving Out",
  "desc": "Move-out process, bond refund",
  "questions": [
    {
      "q": "What is the move-out process?",
      "blocks": [
        {"t": "The PM will send you a vacate guide with move-out notes and 【exit cleaning booking】. Our partnered cleaners will redo any covered items that have issues, so choose the full service to minimise back-and-forth. Note that cleaning and defects are separate — e.g. a stained carpet cannot be washed out; that's a defect, not a cleaning issue. Get a receipt from the cleaner before paying; we need the cleaning receipt to arrange your bond refund."},
        {"t": "After the 【exit clean】, don't disconnect power before moving out, or we can't inspect the property. You can disconnect electricity yourself after 5 working days."},
        {"t": "We complete the 【exit inspection】 within 5 working days and send you any property issues. Items you purchased (covered) can be re-cleaned free; uncovered items require you to re-clean or compensate for the defect."},
        {"t": "You'll also need to sign a consent form with the new incoming tenant to divide responsibility."},
        {"t": "Once everything is resolved, we apply to release your RTBA bond within 10 working days. When you receive the RTBA email, click through and enter your bank details to receive the bond. That completes the move-out process."},
      ],
    },
  ],
},
]

FOOTER = "Please contact your Property Manager if you have any questions"
SITE_BRAND = "Aurora × Protique Real Estate"
SITE_NAME = "Tenant Handbook"
SITE_TITLE = SITE_BRAND + " " + SITE_NAME
SITE_SUB = "Please read before moving in. Check here first, then contact your Property Manager."
