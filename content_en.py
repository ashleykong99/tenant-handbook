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
  "desc": "Front desk, access, parcels, facilities, moving and waste",
  "questions": [
    {
      "q": "Building Front Desk & Key Contacts",
      "blocks": [
        {"t": "Concierge or security staff are available at the front desk 24 hours a day. Current service hours are:"},
        {"list": [
          "concierge: daily, 7:00am–11:00pm",
          "Security: daily, 11:00pm–7:00am",
          "Building Manager's Office: Monday–Friday, 9:00am–5:00pm",
          "For emergencies or matters requiring urgent attention, contact the front desk first, and the front desk will refer the matter through the management system",
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
        {"t": "All residents must register for the WeWumbo app to access:"},
        {"list": [
          "Identity verification",
          "Facility and moving lift bookings",
          "Parcel notifications",
          "Building announcements",
          "Other building service requests",
        ]},
        {"h": "When Registering"},
        {"list": [
          "Select Tenant or Owner",
          "New residents select 【Moving In】; existing residents select 【Existing】",
          "Select your zone: Stratus (Levels 10–30) / Cumulus (Levels 32–60) / Australis (Levels 63–85)",
          "Upload a valid photo ID",
          "Tenants must upload their Lease Agreement",
        ]},
      ],
    },
    {
      "q": "Moving In & Moving Out",
      "blocks": [
        {"h": "Booking Requirements"},
        {"list": [
          "Book the Move In/Out Lift & Loading Dock through WeWumbo",
          "Book at least 8 hours in advance",
          "Without a booking, the building may refuse the move",
          "Confirm your lift time slot before booking a removalist",
        ]},
        {"h": "Allowed Moving Times"},
        {"list": [
          "Monday–Saturday: 9:00am–5:30pm",
          "Moving is not permitted on Sundays or public holidays",
          "Each booking may be up to 3 hours",
        ]},
        {"h": "Moving Lifts"},
        {"table": {
          "header": ["Levels", "Lift", "Internal Dimensions", "Door Opening"],
          "rows": [
            ["10–60", "Lift C", "1800L × 2100W × 2600H mm", "1300W × 2100H mm"],
            ["63–85", "Lift G", "1400L × 2000W × 2700H mm", "1100W × 2100H mm"],
          ],
        }},
        {"t": "These dimensions exclude the lift's protective padding, so allow extra clearance for furniture."},
        {"h": "On Moving Day"},
        {"list": [
          "Removal trucks must enter the loading dock via Little La Trobe Street",
          "The resident and removalist must first register with the concierge",
          "Collect the relevant keys and moving route instructions",
          "Notify the concierge and return the keys when finished",
          "All packaging materials and moving waste must be removed by the resident or removalist",
          "The resident must pay the cost of repairing any damage to areas such as the Loading Dock, lifts, lift lobbies and corridors",
        ]},
        {"t": "If the rules are not followed, the building may refuse the move and will not be responsible for removalist cancellation fees, waiting fees or any other losses."},
      ],
    },
    {
      "q": "Access, Keys & Intercom",
      "blocks": [
        {"h": "Intercom"},
        {"t": "When a visitor enters your apartment number and calls through the intercom:"},
        {"list": [
          "Press Answer to take the call",
          "Press 【Door Release & Lift Release】 to unlock the entry door for approximately 5 seconds and enable lift access for approximately 180 seconds",
          "The lift will only allow the visitor to select your floor",
        ]},
        {"h": "Keys & Access"},
        {"list": [
          "Apartment key: provides access to your apartment",
          "Fob: provides access to the building, lifts and facilities",
          "Car park remote: opens the car park roller door",
        ]},
        {"h": "Note"},
        {"list": [
          "If you are locked out, contact your Property Manager",
        ]},
      ],
    },
    {
      "q": "Parcels & Food Delivery",
      "blocks": [
        {"h": "Delivery Address Format"},
        {"t": "Your delivery details must include:"},
        {"list": [
          "Recipient's full name",
          "Mobile number",
          "Full address, e.g.: 8601/228 La Trobe Street, Melbourne VIC 3000",
        ]},
        {"t": "Incomplete details may cause a parcel to be delayed or lost."},
        {"h": "Small Parcels"},
        {"list": [
          "Usually placed in your mailbox by the courier",
          "You may not be notified, so check your mailbox regularly",
          "Renters who lose their mailbox key should contact us; owners can contact the front desk",
        ]},
        {"h": "Medium Parcels"},
        {"list": [
          "The front desk registers the parcel in WeWumbo",
          "You will receive a collection notification through the app",
          "You must be registered on WeWumbo to receive notifications",
          "Parcels not collected within 28 days will be returned to the sender",
        ]},
        {"h": "Large Parcels (Accepted by the Front Desk Only Within These Limits)"},
        {"list": [
          "Must weigh no more than 15kg",
          "Must be no larger than 550mm × 300mm × 300mm",
          "Must be collected within 3 days of receiving the SMS",
          "Overdue parcels will be returned to the sender",
        ]},
        {"h": "Furniture, Appliances and Other Items That Exceed the Limits"},
        {"list": [
          "The front desk may contact you, but you must arrange prompt collection from the loading dock",
          "Multiple large items may require a moving-lift booking",
          "The front desk may refuse delivery if you cannot collect the item in time",
          "Residents should notify the front desk in advance when expecting a delivery; for oversized items, someone else must still be arranged to accept delivery",
        ]},
        {"h": "Important Disclaimer"},
        {"list": [
          "Building management is not responsible for loss, damage or theft after a parcel has been handed to the front desk",
          "Valuables should be received in person wherever possible",
        ]},
        {"h": "Food Delivery"},
        {"list": [
          "The front desk does not accept food, takeaway or fresh groceries",
          "Track your delivery and collect it in the lobby in person",
          "The building is not responsible for spoilage or loss caused by failure to collect promptly",
        ]},
      ],
    },
    {
      "q": "Noise Restrictions",
      "blocks": [
        {"t": "Residential noise is prohibited during the following hours:"},
        {"table": {
          "header": ["Day", "Restricted Hours"],
          "rows": [
            ["Monday–Thursday", "Before 7:00am and after 10:00pm"],
            ["Friday", "Before 7:00am and after 11:00pm"],
            ["Saturday and public holidays", "Before 9:00am and after 11:00pm"],
            ["Sunday", "Before 9:00am and after 10:00pm"],
          ],
        }},
        {"t": "Even outside these hours, prolonged or excessive noise may still be unreasonable."},
        {"h": "If You Experience Noise"},
        {"list": [
          "Contact the concierge or security immediately",
          "Record the time and type of noise, and capture audio or video where possible",
          "The front desk or security will investigate and give a verbal warning",
          "Ongoing incidents will be escalated to the Owners Corporation",
          "Serious or ongoing noise may be reported to the police",
        ]},
      ],
    },
    {
      "q": "Smoking & Common Areas",
      "blocks": [
        {"h": "No Smoking or Vaping"},
        {"t": "Smoking or vaping is strictly prohibited in these common areas:"},
        {"list": [
          "Corridors",
          "Lobby and lift lobbies",
          "Car park and basement areas",
          "Fire stairs",
        ]},
        {"t": "A breach may trigger the fire alarm and result in a Breach Notice."},
        {"t": "If cooking or smoking inside the apartment:"},
        {"list": [
          "Do not open the entry door to ventilate",
          "Open the windows for ventilation",
          "Smoke entering the common corridors may trigger the building fire alarm",
        ]},
        {"h": "Common Areas"},
        {"list": [
          "No littering",
          "No doormats, shoes or personal items",
          "Fire escape routes must stay clear",
          "Common-area power outlets are for building maintenance only",
          "Not for private use or EV charging",
          "A breach will result in a Breach Notice",
        ]},
      ],
    },
    {
      "q": "Facilities & Opening Hours",
      "blocks": [
        {"t": "The facilities available to you depend on your floor:"},
        {"table": {
          "header": ["Resident Zone", "Facility Levels"],
          "rows": [
            ["Stratus 10–30", "Level 8"],
            ["Cumulus 32–60", "Levels 8 & 61"],
            ["Australis 63–85", "Levels 8, 61 & 86"],
          ],
        }},
        {"t": "Bookings for all facilities that require a booking must be approved through WeWumbo."},
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
          "Facilities are for residents and their invited guests only",
          "Facilities must not be sold, booked or rented to external parties",
          "The booking resident must be present at all times",
          "Register with the concierge and sign the confirmation form before use",
          "The same company may book the same room only once per day",
          "No consecutive bookings",
          "Each facility may be booked up to 5 times per month",
          "Under-16s must be accompanied by an adult",
          "Clean up and dispose of rubbish after use",
          "Residents are responsible for their guests' behaviour",
          "The booking resident must pay for any damage to the facilities",
          "No decorations fixed to walls, doors or other surfaces",
          "Switch off the power, gas, air conditioning and lights before leaving",
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
          "Wet clothing, shoes and socks must not be taken outside the pool area",
          "Nude swimming is prohibited",
        ]},
        {"t": "Use of the steam room or sauna is not recommended for pregnant people or anyone with a heart, circulatory, respiratory, blood pressure, diabetes or kidney condition. After drinking alcohol, eating or exercising, wait until your body has recovered before using them."},
      ],
    },
    {
      "q": "Waste Disposal",
      "blocks": [
        {"t": "At the time this handbook was published, the rubbish chute was temporarily unavailable. The current requirements are:"},
        {"list": [
          "Do not leave rubbish in the bin room, rubbish chute or common areas on your floor",
          "General waste and recyclables must go to B1",
          "Tie rubbish bags securely and double-bag them to prevent liquids from staining the carpet",
          "Large cardboard boxes must be flattened",
          "Do not put furniture, appliances or bulky items in general bins",
          "Nitrous oxide canisters / nang canisters must not be put in general waste, recycling bins or the bulky waste area; contact the supplier for disposal",
          "Do not leave rubbish on the ground",
        ]},
        {"h": "Lifts to B1"},
        {"list": [
          "Lift C: lower and mid-rise residents",
          "Lift G: high-rise residents",
        ]},
        {"t": "On weekdays between 9:00am and 6:00pm, Lifts C and G may be locked for moving bookings. It is therefore recommended that rubbish be taken out 【between 6:00pm on a weekday and 9:00am the next day】; the lifts are usually available all day on Sundays and public holidays."},
        {"h": "Bulky Waste"},
        {"list": [
          "Collected on the first Saturday of each month",
          "Items should be placed in the designated B1 area only on the collection date",
        ]},
        {"h": "E-waste"},
        {"list": [
          "Place items in the e-waste bin near the bulky waste area",
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
  "desc": "Furniture, cleaning and furniture replacement",
  "questions": [
    {
      "q": "What should I do with small items or furniture I do not want?",
      "blocks": [
        {"t": "Tell your Property Manager which items you do not want and ask her to send you the 【original property report】. This report records the property's condition when it was rented out. Do not remove or dispose of any furniture or items without the Property Manager's written consent, even if they do not appear in the report. Note: we will advise you separately in special circumstances, such as when furniture has been replaced or the landlord has added new furniture."},
      ],
    },
    {
      "q": "The property seems a little dirty. Can the landlord / previous tenant reimburse the cleaning cost or arrange for it to be cleaned again?",
      "blocks": [
        {"t": "All properties have been professionally cleaned and the carpets steam cleaned before the keys are handed over. You may ask the Property Manager to provide the cleaning receipt as proof."},
        {"t": "Please note that everyone has different cleaning standards. We have inspected the property and it has passed our cleaning standard. Situations that may arise include: a lot of dust being vacuumed from a carpet that does not look clean (it is normal for a wool carpet to shed a lot of fibres); opening windows or entering with shoes can cause hidden dust / hair; and sweat stains on mattresses are also difficult to avoid—if this particularly concerns you, you can provide your own mattress protector. If there is obvious grease on a benchtop or a large stain on a mattress, we will arrange for the cleaner to return."},
      ],
    },
    {
      "q": "Can I replace a mattress, sofa or other item of furniture?",
      "blocks": [
        {"t": "We understand that everyone has their own furniture preferences. If you strongly wish to replace an item, first find a product that is 【highly similar】 in style and price to the current furniture and send it to the Property Manager for approval. Once permission is given, arrange disposal yourself (following the steps above) and arrange for the new furniture to be brought in (remember to contact the building BM or front desk to book the lift; the PM is not responsible for this)."},
      ],
    },
  ],
},
{
  "id": "maintenance",
  "emoji": "🔧",
  "title": "Maintenance",
  "desc": "Digital locks, appliances, plumbing, electrical and more",
  "note": "Before reporting any repair: read this handbook and follow the instructions. If the item still does not work, take photos and videos and send them to Protique Xiao Nan on WeChat at Protique-leasing / WhatsApp 0422329166",
  "questions": [
    {
      "q": "Something is broken — how do I report it?",
      "blocks": [
        {"t": "If you discover the issue just after moving in, it may be a problem we already know about and are discussing with the previous tenant, or we may be waiting for a tradesperson to repair / replace it. If you discover the issue later in the tenancy (more than 5 business days after moving in), you can report it to the PM and 【attach photos and videos】. We will complete non-urgent repairs within the legally prescribed 14 days and aim to complete urgent repairs within two days. The distinction between urgent and non-urgent is 【whether the issue affects minimum rental standards】, including but not limited to water leaks / explosions / the cooktop being completely unusable / the toilet being completely unusable / being unable to shower. Specific details can be looked up online. As labour is expensive in Australia, some repairs require tenants to assist with preliminary troubleshooting. Possible issues are listed one by one below."},
        {"t": "For non-urgent repairs, submit a written request to your Property Manager. The time required to respond and complete the repair depends on the specific issue, access arrangements, parts availability and the repairer's schedule."},
        {"h": "When reporting a repair, please include"},
        {"list": [
          "Property address",
          "Renter's name",
          "Problem description",
          "When it started",
          "Photos",
          "Video showing the issue",
          "Error code / model number",
          "Available access times",
          "Whether the property is currently safe",
        ]},
      ],
    },
    {
      "q": "How do I change the digital lock passcode?",
      "blocks": [
        {"t": "First use the key to open the door. With the 【front door open】, follow the video and document below step by step. The initial passcode is 【1234#】."},
        {"media": [
          V("10q6Lu4rwoRRwhxUf3HQlqSS0yU2d8T1F", "Digital lock setup video"),
          P("19ld0-78T3KH2O7qqolz6wZoATfWT8N5C", "assets/cover-samsung-lock.png", "Samsung digital lock form"),
        ]},
      ],
    },
    {
      "q": "A light is not working — what should I do?",
      "blocks": [
        {"t": "There are two possibilities. The first is an electrical circuit problem; we will send an electrician to inspect and repair it, and the landlord will pay the cost. The second is simply that the light globe has failed, which is a tenant-use issue—we can help contact a tradesperson to replace it. The tradesperson's minimum call-out fee is $80+GST; if there are other jobs at the same time, each light globe is charged separately at $40+GST. The tenant must pay these costs. You may also choose to replace it yourself:"},
        {"media": [
          V("15hbjoq_0KgoOCE3WKCJICMTqDTT0JprM", "Light globe replacement tutorial"),
        ]},
      ],
    },
    {
      "q": "What should I do if a window will not open or stay open?",
      "blocks": [
        {"t": "Tighten the screw as shown in the image below. If this still does not work, ask the apartment front desk, which can assist with the repair."},
        {"media": [
          IMG("assets/img-window.jpg", "Window screw location"),
        ]},
      ],
    },
    {
      "q": "The fridge is not working — what should I do?",
      "blocks": [
        {"t": "There are two possibilities. First, if the fridge keeps making noise but cooling is unaffected, press and hold its power button if it has one; otherwise, turn off the circuit breaker and restart it. Second, if the fridge is not cooling / freezing, the most common cause is ice blocking the air duct or vent. Most fridges use a single evaporator and fan to circulate cold air. Cold air is produced by the evaporator and then blown through air ducts to the different compartments. If too much frost forms on the evaporator or the air duct freezes, the fridge will not cool."},
        {"t": "Solution: 【completely disconnect the fridge from power for 24–36 hours and leave the doors open so that the ice fully melts】 (preferably unplug it; if an integrated fridge cannot be unplugged, turn off the circuit breaker). When the time is up, dry the inside of the fridge, reconnect the power and test whether it has recovered."},
        {"t": "If there is excessive ice in the freezer compartment, the drain may be blocked. You can try cleaning it:"},
        {"media": [
          V("1g6WxgFTSYjQL9rfoyLt0owcR902clmMc", "Fridge drain clearing video"),
        ]},
        {"t": "If it has not recovered, contact the PM and we will arrange a repair / replacement."},
      ],
    },
    {
      "q": "What should I do if the cooktop is not working?",
      "blocks": [
        {"t": "For an induction cooktop, first check whether the power under the cabinet is switched on. For a cooktop, after confirming that the electricity and gas are connected, there are two possibilities. First, if the flame goes out as soon as you release the knob and will not stay lit, collect a piece of 【sandpaper】 from the office and use it to polish the small white pin to restore the flame. Second, if turning the knob only produces a hissing sound and a very small flame, the gas outlet is blocked. Collect a 【low-flame needle】 from the office and use it to clear the blocked opening. These are tenant-use issues. Always clean the cooktop promptly after cooking, do not let oil seep into the gas burner, and do not use an alcohol-based cleaner."},
        {"media": [
          IMG("assets/img-cooktop-no-fire.jpg", "Cooktop no-fire guide"),
          V("1TfzbCQej1cJsEDMsJCqvTVEDzqxWi2C-", "Cooktop ignition tutorial"),
          V("1p5qEv5h_UjQKJ4s93oi_wvxZEe9pZU6J", "Cooktop ignition tutorial 2"),
          V("1yOCBIX8n1i8qzBpzsAVF3z7-wXl7zOuj", "Gas stove igniter not working"),
        ]},
        {"t": "If the attempts above still do not resolve the issue, contact the PM."},
      ],
    },
    {
      "q": "What should I do if the oven light is not working?",
      "blocks": [
        {"t": "A failed light does not affect use. If the oven is unusable, this will be explained before the tenant moves in."},
      ],
    },
    {
      "q": "The dishwasher is not working — what should I do?",
      "blocks": [
        {"t": "First check whether the power under the cabinet is connected. An error code will appear on the display. Search online using the error code + model + brand to find the corresponding possible causes and solutions. The most common problem is a blocked outlet preventing drainage. Remove and clean the water pipe cover and filter, then press and hold the power button for 15 seconds to restart the dishwasher. These situations are tenant-use issues."},
        {"media": [
          V("12jejWAY8s244tBrLs312Jz1FsPUOPVoG", "Miele dishwasher cleaning"),
          V("1ZgCpZpMIQ81oaO9S1OPsiaf_rjucRzWT", "Miele upper rack adjustment"),
          V("1-YJOd2ElwhrLuucDoVVnZKmg6Sk0BdyZ", "Fisher & Paykel cleaning"),
          D("1A0CVc8c2OmZiQ_5wCKFCgSl3vcqO_RKaSXbunuWIoSE", "Fisher & Paykel not draining"),
          V("164lrzpDHoRzS9UkwIlzo3k6y0z7_vmUt", "Upper water supply hose dropped"),
          D("1qEuq0doK2qSCWKhv3YhA158wyZvyxaFPITm1IaIOpJs", "Cleaning the dishwasher"),
        ]},
        {"t": "If this still does not resolve the issue, contact the PM."},
      ],
    },
    {
      "q": "What should I do if the washing machine is not working?",
      "blocks": [
        {"t": "First check whether the power is connected / the switch is on. An error code will appear on the display; search online using the error code + model + brand. First try restarting it: switch it off, unplug it, wait 5–10 minutes, then plug it back in and start it. Sometimes the system simply needs to be reset. Will not start → check whether the door is fully closed; will not spin → check whether there are too many clothes / they are concentrated on one side; will not drain → check whether the filter is blocked (open the small door at the bottom of the machine) or the drain hose is blocked. These are tenant-use issues."},
        {"media": [
          IMG("assets/img-laundry.jpg", "Laundry room diagram"),
          V("1gZ7EuWBbN5ZPP2b9ErOBNnLFzwRzMx0t", "Washing machine cleaning and maintenance"),
          V("1ASLRslNYOCZ8NmpeFTQgoWc6W99qRb89", "No power? Troubleshooting"),
          V("1uo4m5SFIa1A0-8qp9tQuzNoE7i6zMwFM", "U-bend installation"),
          V("1qfqrjvO1rZsWNLQnXrzBw34b2DysZdLg", "Draining / filter cleaning"),
          V("1z7tjaUOePG0p2BEZ7dPLqEYn8AXrSnb3", "Door seal gap"),
        ]},
        {"t": "If this still does not resolve the issue, contact the PM."},
      ],
    },
    {
      "q": "What should I do if the dryer is not working?",
      "blocks": [
        {"t": "First check whether the power is connected / the switch is on. An error code will appear on the display. First try restarting it: switch it off, unplug it, wait 5–10 minutes, then plug it back in. Will not start → check whether the door is fully closed; will not spin → check whether there are too many clothes or the drainage tank is full (simply pull out the top drawer); will not drain → check whether the filter is blocked (at the bottom or side of the rubber seal connection), remove the filter and clean out the lint, then try again. These are tenant-use issues. If this still does not resolve the issue, contact the PM."},
        {"media": [
          P("1wpSqOSXvgzWKwaHOw7JQvMDw7t53Q5yI", "assets/cover-miele-dryer-06086650.png", "Miele dryer manual"),
          P("1yHWQ7s48-vQaUrQoS9z35WNJctMElNQW", "assets/cover-miele-dryer-manual.png", "Miele dryer user manual (English)"),
        ]},
      ],
    },
    {
      "q": "What should I do if the basin will not drain?",
      "blocks": [
        {"t": "This is generally caused by hair tangling / blocking the drain and is a tenant-use issue—remember not to wash your hair in the basin! You need to buy a bottle of Drano (the large orange bottle):"},
        {"media": [
          P("1eS0Tf8Zw1bi0DwT9hVaC0IhK2RSoplzX", "assets/cover-drainage.png", "Drain blockage guide"),
        ]},
        {"t": "When the basin is dry, pour in half the bottle. Wait 12 hours, then flush it with hot water for several minutes. If this still does not resolve the issue, contact the PM."},
      ],
    },
    {
      "q": "What should I do if the toilet is leaking or will not flush?",
      "blocks": [
        {"t": "First open the toilet lid and turn off the water valve to stop further leaking. Then contact the PM to resolve the issue."},
      ],
    },
    {
      "q": "What should I do if the toilet seat is misaligned?",
      "blocks": [
        {"media": [
          V("1ugDYpdDQ_6Jl0Q5IOWOJOHvo2kB2mkzM", "Toilet lid removal"),
          V("1Lho8xOBrzWpeMKdEt-iSOO9xMYGBbhNc", "Toilet repair guide"),
          V("14Cd9tVAQ3oTwm0lyQl7L0AUiqYXjisBk", "Loose toilet seat"),
        ]},
      ],
    },
    {
      "q": "What should I do if the tap has fallen off / the basin button will not pop up?",
      "blocks": [
        {"media": [
          V("1RSAiAElSkCmBzKP2U3M28KjO7JIx6u9a", "Tap repair"),
          V("1iNE2jtgXa6JO76-Mw5oDUHaFR5uqeSua", "Basin button stuck"),
        ]},
      ],
    },
    {
      "q": "What should I do if the air conditioner is not working?",
      "blocks": [
        {"t": "If an error code appears on the panel, contact the front desk to restart the main unit. Clean the air-conditioner filter if necessary:"},
        {"media": [
          V("1ndRNfxaL47Gd6fEthOzQwarDRC_TQTo_", "AC filter removal & cleaning"),
        ]},
      ],
    },
    {
      "q": "What should I do if the bed frame has collapsed?",
      "blocks": [
        {"t": "Follow the repair video instructions:"},
        {"media": [
          V("1ImyJ3kPlclJmEN_Th_kA8Ak_9-yrZKEc", "Bed frame repair"),
        ]},
        {"t": "If this still does not resolve the issue, contact the PM."},
      ],
    },
    {
      "q": "What should I do if the smoke alarm is not working or keeps beeping?",
      "blocks": [
        {"t": "The battery may be flat and need to be replaced, or the alarm may need to be reset:"},
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
  "desc": "Lost keys and other emergencies",
  "questions": [
    {
      "q": "I have lost a key — what should I do?",
      "blocks": [
        {"t": "First, confirm whether you have lost the fob access card (the round disc used for the lifts), the hard key (the metal key used to open your apartment door), or the mailbox key."},
        {"t": "If you have lost the fob, take a photo of any remaining fob and check whether there is a numerical code on the back. Two separate payments are required: $95 to O Real Investment Trust (BSB 033002, Acc 037975), and $110 to O REAL (BSB 733003, Acc 727393). Once we receive screenshots of the transfers, we will order a replacement from the building. It is usually available within two weeks."},
        {"t": "If you have lost the hard key, it cannot be reordered and a replacement charge of $200 applies."},
        {"t": "If you have lost the mailbox key, transfer $25.3 and we will order a replacement from a locksmith."},
      ],
    },
    {
      "q": "What should I do during a power outage?",
      "blocks": [
        {"list": [
          "Check whether the Master Switch near the front door is on",
          "Check whether the Circuit Breaker is on",
          "If it has tripped, unplug the appliance causing the problem before switching it back on",
          "If it trips again: tenants should contact the agent; owners should contact an electrician",
          "If the switches are normal but there is still no power, contact the Origin Energy emergency hotline",
        ]},
      ],
    },
    {
      "q": "Fire & Emergency Evacuation",
      "blocks": [
        {"h": "Assembly Point"},
        {"t": "The fire evacuation assembly point is the 【State Library Victoria Forecourt】."},
        {"t": "The spiral staircase on the mezzanine of each level leads to the fire escape door. Residents should follow the fire evacuation instructions."},
        {"h": "Lower & Mid-rise Residents (Levels 10–60)"},
        {"list": [
          "Do not search for the fire source or collect belongings during a fire alarm",
          "Check the door and handle with the back of your hand before opening",
          "Use the stairwell to access the fire stairs",
          "Do not use the lifts",
          "Follow the Fire Warden's instructions",
          "If the exit / stairs are blocked by smoke, call the Royal Call Centre",
          "If assistance is required, use the emergency phone inside the door on each level",
          "Do not re-enter the building until permitted",
        ]},
        {"h": "High-rise Residents (Levels 63–85)"},
        {"list": [
          "During a fire alarm, the high-rise lifts may be used for evacuation if permitted by the emergency instructions",
          "If there is heavy smoke, use the fire stairs to reach the Refuge Areas on Level 61",
          "The refuge areas on Level 61 include the Cumulus Lounge, Games Lounge and Wine Cellar",
          "These areas have independent systems for communication, and fire doors where people can wait",
        ]},
      ],
    },
    {
      "q": "Preventing False Alarms",
      "blocks": [
        {"list": [
          "Do not place cookware or ovens near smoke detectors, and do not obstruct fire extinguishers, fire doors or sprinkler heads",
          "Do not cover smoke detectors",
          "When cooking produces smoke, open the windows for ventilation to prevent kitchen smoke from triggering the alarm",
          "Familiarise yourself with the fire plan and evacuation routes in advance",
        ]},
        {"h": "Smoke Alarms Inside Apartments"},
        {"list": [
          "Generally located on the corridor ceiling outside the bedroom",
          "Usually not connected to the building's active fire protection system",
          "It will sound its own alarm when it detects smoke (usually not controlled by the fire brigade / building management)",
          "However, it should be dealt with promptly and taken seriously",
          "Do not cover or remove the detector",
        ]},
        {"h": "Common-area Sounders"},
        {"t": "Common-area sounders are connected to the building fire system; once triggered, they automatically notify the fire brigade. Therefore, when an alarm sounds, never open the apartment door to investigate the cause."},
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
      "q": "Who should I contact for urgent repairs on weekends or public holidays?",
      "blocks": [
        {"t": "On weekends or public holidays, if the Property Manager cannot be reached and there is an urgent repair (urgent situations only, such as a water leak, electrical leakage or being locked out without your keys), contact the following repairers:"},
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
  "title": "Rental Agreements and Subletting",
  "desc": "Renewals, adding a housemate and subletting",
  "questions": [
    {
      "q": "My rental agreement is expiring — can I renew it?",
      "blocks": [
        {"t": "Generally, if the landlord has no other plans, and you have lived in the property responsibly, caused no damage and kept it clean and tidy, you can renew for one year or half a year. Ask the PM about the specific arrangements."},
      ],
    },
    {
      "q": "I have a new housemate — how do I add them to the rental agreement?",
      "blocks": [
        {"t": "Yes. Send your housemate's details to your Property Manager for assessment: passport or driver's licence; visa and Confirmation of Enrolment (COE), or Medicare card; bank statement or payslip; and a completed application form. Once the application is approved, we will prepare a new rental agreement. Any related fee will be limited to the reasonable actual cost and confirmed in writing."},
      ],
    },
    {
      "q": "I cannot continue my rental agreement due to circumstances beyond my control — what should I do?",
      "blocks": [
        {"t": "You may find a replacement renter to take over the rental agreement. A transfer fee may apply, as specified in your rental agreement. Once a replacement renter has been confirmed, the fee may be paid separately or deducted from the bond after you move out."},
        {"t": "You may advertise on online social media yourself, or ask us to advertise the property through channels such as realestate.com and Domain. The advertising fee is a one-off payment of $330, payable in advance to O REAL (BSB 733003, Acc 727393)."},
        {"t": "Please note that paying the advertising fee does not guarantee that we will find a replacement renter. The outgoing renter remains responsible for rent and any related costs until the new rental agreement begins or the existing rental agreement otherwise legally ends."},
      ],
    },
    {
      "q": "I have found someone to take over the rental agreement — what happens next?",
      "blocks": [
        {"t": "Send the proposed replacement renter's details to your Property Manager for assessment: passport or driver's licence; visa and Confirmation of Enrolment (COE), or Medicare card; bank statement or payslip; and a completed application form. Once the application is approved, we will prepare a new rental agreement. After the replacement renter has signed the agreement and paid the bond and first month's rent, you can pay the transfer fee and arrange the move-out process."},
      ],
    },
  ],
},
{
  "id": "move-out",
  "emoji": "🔑",
  "title": "Moving Out",
  "desc": "Move-out process and bond refund",
  "questions": [
    {
      "q": "What is the move-out process?",
      "blocks": [
        {"t": "Your Property Manager will send you a vacate guide containing the move-out instructions and information about 【booking end-of-lease cleaning】. We can recommend one of our preferred cleaning companies. Choosing the full cleaning service can reduce the need for repeated follow-up. Cleaning issues and defects are assessed separately. For example, a carpet stain that cannot be removed through cleaning is considered a defect and is not the cleaner's responsibility. You must return the property in a reasonably clean condition, taking into account its condition when you moved in. If professional cleaning or carpet steam cleaning is required under your rental agreement or in your circumstances, keep the receipt as evidence."},
        {"t": "After the 【end-of-lease cleaning】 has been completed, remember not to disconnect the electricity before moving out, otherwise we will be unable to inspect the property. You may disconnect the electricity yourself after 5 working days."},
        {"t": "We will complete the 【exit inspection】 within 5 working days and notify you of any issues with the property. If an issue relates to an item included in the cleaning service you purchased, the cleaner can return and clean it again at no additional charge. If the item was not included, you will need to clean it again or compensate for the defect."},
        {"t": "You and the incoming renter will also need to sign a consent form to clarify responsibility for the condition of the property."},
        {"t": "Once all issues have been resolved, we will apply to release your bond held by the RTBA within 10 working days. When you receive an email from the RTBA, follow the link and enter your bank account details. You can then wait for the bond to be deposited into your account. This completes the move-out process."},
      ],
    },
  ],
},
]

FOOTER = "Please contact your Property Manager if you have any questions"
SITE_BRAND = "Aurora × Protique Realty"
SITE_NAME = "Tenant Handbook"
SITE_TITLE = SITE_BRAND + " " + SITE_NAME
SITE_SUB = "Please read before moving in. Check here first, then contact your Property Manager."
