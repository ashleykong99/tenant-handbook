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
          "For urgent building matters, contact the front desk. If anyone is in immediate danger, call 000 first. For urgent repairs inside the apartment, also follow the urgent repair process below",
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
          "Select Renter or Owner",
          "New residents select 【Moving In】; existing residents select 【Existing】",
          "Select your zone: Stratus (Levels 10–30) / Cumulus (Levels 32–60) / Australis (Levels 63–85)",
          "Upload a valid photo ID",
          "Renters must upload the relevant pages of their rental agreement, as required by building management",
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
          "Without a confirmed booking, building management may not permit access to the moving lift or loading dock",
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
          "The resident may be responsible for damage caused by the resident, their removalist or their guests, subject to evidence and applicable law",
        ]},
        {"t": "Failure to follow the building's booking and access rules may result in access being delayed or refused. Responsibility for any resulting costs will depend on the circumstances and applicable law."},
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
        {"t": "Incomplete details may delay delivery or prevent the courier from completing the delivery."},
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
          "Parcels left uncollected for 28 days may be returned to the sender under the building's current parcel policy",
        ]},
        {"h": "Large Parcels (Accepted by the Front Desk Only Within These Limits)"},
        {"list": [
          "Must weigh no more than 15kg",
          "Must be no larger than 550mm × 300mm × 300mm",
          "Must be collected within 3 days of receiving the SMS",
          "Parcels not collected by the deadline may be returned to the sender under the building's current parcel policy",
        ]},
        {"h": "Furniture, Appliances and Other Items That Exceed the Limits"},
        {"list": [
          "The front desk may contact you, but you must arrange prompt collection from the loading dock",
          "Multiple large items may require a moving-lift booking",
          "The front desk may refuse delivery if you cannot collect the item in time",
          "Notify the front desk before the parcel arrives if you are overseas",
        ]},
        {"h": "Important Disclaimer"},
        {"list": [
          "Building management does not guarantee the security or condition of parcels held at the front desk. Any liability will depend on the circumstances and applicable law",
          "Valuables should be received in person wherever possible",
        ]},
        {"h": "Food Delivery"},
        {"list": [
          "The front desk does not accept food, takeaway or fresh groceries",
          "Track your delivery and collect it in the lobby in person",
          "Residents should collect food promptly. Responsibility for spoilage or loss will depend on the circumstances",
        ]},
      ],
    },
    {
      "q": "Noise Restrictions",
      "blocks": [
        {"t": "Certain types of residential noise must not be audible in neighbouring homes during the restricted hours below. Unreasonable noise may also be prohibited at other times:"},
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
          "The front desk or security may investigate and, where appropriate, speak to the resident involved",
          "Persistent issues may be escalated to building management or the Owners Corporation",
          "Serious or ongoing noise may be reported to the appropriate authority, such as the police, local council or building management, depending on the circumstances",
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
        {"t": "Smoke or vapour may trigger an alarm. A breach of the building rules or rental agreement may result in appropriate follow-up or a formal notice."},
        {"t": "When cooking, use the rangehood and keep smoke out of common areas. Follow the rental agreement and building rules regarding smoking:"},
        {"list": [
          "Do not open the entry door to ventilate",
          "Use appropriate ventilation, such as the rangehood or windows",
          "Smoke entering the common corridors may trigger the building fire alarm",
        ]},
        {"h": "Common Areas"},
        {"list": [
          "No littering",
          "No doormats, shoes or personal items",
          "Fire escape routes must stay clear",
          "Common-area power outlets are for building maintenance only",
          "Not for private use or EV charging",
          "Breaches may be addressed under the building rules or rental agreement and may result in a formal notice from the authorised party",
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
          "Do not sell bookings, book on behalf of others or hire facilities to external parties",
          "The booking resident must be present at all times",
          "Register with the concierge and sign the confirmation form before use",
          "Each apartment may only book the same room once per day",
          "No consecutive bookings",
          "Each facility may be booked up to five times per month",
          "Under-16s must be accompanied by an adult",
          "Clean up and dispose of rubbish after use",
          "Residents are responsible for their guests' behaviour",
          "The booking resident may be charged for damage caused by the resident or their guests, subject to evidence and the building rules",
          "No decorations fixed to walls, doors or other surfaces",
          "Switch off any appliances, cooking equipment, air conditioning and lights used during the booking",
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
          "Appropriate swimwear must be worn at all times",
        ]},
        {"t": "Follow the posted health and safety instructions. If you are pregnant, have a medical condition or are unsure whether the steam room or sauna is suitable for you, seek medical advice. Do not use these facilities while affected by alcohol or if you feel unwell."},
      ],
    },
    {
      "q": "Waste Disposal",
      "blocks": [
        {"t": "The rubbish chute is currently unavailable. Check WeWumbo or current building notices before relying on this information. While the chute remains unavailable:"},
        {"list": [
          "Do not leave rubbish in the bin room, rubbish chute or common areas on your floor",
          "General waste and recyclables must go to B1",
          "Tie rubbish bags securely and double-bag them to prevent liquids from staining the carpet",
          "Large cardboard boxes must be flattened",
          "Do not put furniture, appliances or bulky items in general bins",
          "Do not place nitrous oxide (N2O or nang) canisters in general waste, recycling or bulky waste. Follow current council or building instructions for safe disposal",
          "Do not leave rubbish on the ground",
        ]},
        {"h": "Lifts to B1"},
        {"list": [
          "Lift C: lower and mid-rise residents",
          "Lift G: high-rise residents",
        ]},
        {"t": "Moving bookings may restrict access to B1 between 9:00am and 6:00pm on weekdays. Check lift availability before taking waste to B1. Confirm weekend and public-holiday access with building management."},
        {"h": "Bulky Waste"},
        {"list": [
          "Check the current collection date with building management",
          "Place items in the designated B1 area only during the approved collection period",
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
        {"t": "Tell your Property Manager which items you are concerned about and refer to your 【condition report】. Do not remove, replace or dispose of supplied items without written agreement from the rental provider or Property Manager. Any arrangement for removal, replacement, storage or ownership must be confirmed in writing."},
      ],
    },
    {
      "q": "What should I do if the property was not reasonably clean when I moved in?",
      "blocks": [
        {"t": "Record any cleaning concerns in the condition report and notify your Property Manager promptly. If professional cleaning was arranged, you may ask whether a receipt is available."},
        {"t": "We will assess reported concerns against the property's documented condition and the requirement that it be reasonably clean at the start of the rental agreement. Photograph any dust, hair, stains or hygiene concerns before using the affected area and report them promptly. Where further cleaning is required, the Property Manager will arrange an appropriate response."},
      ],
    },
    {
      "q": "Can I replace a mattress, sofa or other item of furniture?",
      "blocks": [
        {"t": "Before replacing supplied furniture, obtain written agreement covering the replacement item, who will pay for it, who will own it and how the original item will be stored or disposed of. Do not dispose of supplied furniture without written authority. The renter is responsible for complying with the building's current moving and lift-booking requirements."},
      ],
    },
  ],
},
{
  "id": "maintenance",
  "emoji": "🔧",
  "title": "Maintenance",
  "desc": "Door locks, appliances, plumbing & electrical",
  "note": "Report urgent repairs immediately. For non-urgent issues, check the relevant guidance if it is safe to do so, then send helpful photos or videos to Protique Leasing via WeChat or WhatsApp on 0422 329 166.",
  "questions": [
    {
      "q": "Something is broken — how do I report it?",
      "blocks": [
        {"t": "Report all faults promptly, including faults noticed when you move in. We will confirm whether the issue is already being addressed. Urgent repairs are defined by Victorian rental law and include specified serious faults and safety risks. If you are unsure whether a repair is urgent, report it immediately and explain the risk. For non-urgent repairs, send a written request to your Property Manager. Response and completion times depend on the issue, access, parts and contractor availability."},
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
      "q": "How do I change the digital door lock?",
      "blocks": [
        {"t": "First open the door with the key. With the 【door open】, follow the video and document below step by step. If the lock is still using its default code, change it immediately and keep the new code secure."},
        {"media": [
          V("10q6Lu4rwoRRwhxUf3HQlqSS0yU2d8T1F", "Digital lock setup video"),
          P("19ld0-78T3KH2O7qqolz6wZoATfWT8N5C", "assets/cover-samsung-lock.png", "Samsung Digital Locking Form"),
        ]},
      ],
    },
    {
      "q": "A light is not working — what should I do?",
      "blocks": [
        {"t": "Check whether only the globe has failed or whether the circuit or light fitting is affected. Do not attempt electrical work. Responsibility for replacing a globe or repairing a fitting depends on the cause, accessibility and rental agreement. Contact your Property Manager if you are unsure. Any renter-paid cost must be confirmed in writing before work is authorised:"},
        {"media": [
          V("15hbjoq_0KgoOCE3WKCJICMTqDTT0JprM", "Downlight change video"),
        ]},
      ],
    },
    {
      "q": "What should I do if a window will not open or stay open?",
      "blocks": [
        {"t": "Do not force the window or lean outside. If the adjustment shown below is clearly accessible and can be made safely, follow the guide. Otherwise, report the fault to your Property Manager."},
        {"media": [
          IMG("assets/img-window.jpg", "Window screw location"),
        ]},
      ],
    },
    {
      "q": "The fridge is not working — what should I do?",
      "blocks": [
        {"t": "Check the appliance controls and power supply without moving or dismantling the fridge. Only reset a clearly labelled appliance switch or circuit if it is safe to do so. If a circuit trips again, stop and report the fault. Heavy frosting or poor cooling can have several causes."},
        {"t": "Before defrosting, contact your Property Manager unless the appliance manual specifically recommends this step. If instructed to defrost it, move food to safe storage, protect the floor from water and follow the manufacturer's instructions."},
        {"t": "Do not dismantle the appliance. Follow the manufacturer's cleaning instructions or report the fault. The following video is provided only for the applicable model:"},
        {"media": [
          V("1g6WxgFTSYjQL9rfoyLt0owcR902clmMc", "Fridge drain clearing video"),
        ]},
        {"t": "If the fridge still does not work, contact your Property Manager and we will arrange a repair or replacement."},
      ],
    },
    {
      "q": "What should I do if the cooktop is not working?",
      "blocks": [
        {"t": "For an induction cooktop, check the controls and the clearly labelled appliance power switch if it is safe to do so. For a gas cooktop, stop using the burner if the flame will not remain lit or appears abnormal. Do not sand, alter or dismantle components, and do not insert objects into burner jets or gas outlets. If you smell gas, do not operate electrical switches or attempt repairs. Leave the area, call 000 if there is immediate danger, and contact the gas emergency service and your Property Manager. Responsibility for the fault will be assessed after inspection."},
        {"media": [
          IMG("assets/img-cooktop-no-fire.jpg", "Cooktop no-fire guide"),
          V("1TfzbCQej1cJsEDMsJCqvTVEDzqxWi2C-", "Cooktop video 1"),
          V("1p5qEv5h_UjQKJ4s93oi_wvxZEe9pZU6J", "Cooktop video 2"),
          V("1yOCBIX8n1i8qzBpzsAVF3z7-wXl7zOuj", "Gas stove igniter not working"),
        ]},
        {"t": "If these steps do not resolve the issue, contact your Property Manager."},
      ],
    },
    {
      "q": "What should I do if the oven light is not working?",
      "blocks": [
        {"t": "Report a failed oven light or any other fault. Stop using the oven if the fault may affect safe operation, and contact your Property Manager."},
      ],
    },
    {
      "q": "The dishwasher is not working — what should I do?",
      "blocks": [
        {"t": "Check the power supply and record any error code. Refer to the manufacturer's manual for your model. Clean only renter-accessible filters in accordance with the manual; do not disconnect hoses or remove fixed panels. Responsibility for the fault depends on its cause."},
        {"media": [
          V("12jejWAY8s244tBrLs312Jz1FsPUOPVoG", "Miele dishwasher cleaning"),
          V("1ZgCpZpMIQ81oaO9S1OPsiaf_rjucRzWT", "Miele upper rack adjustment"),
          V("1-YJOd2ElwhrLuucDoVVnZKmg6Sk0BdyZ", "Fisher & Paykel cleaning"),
          D("1A0CVc8c2OmZiQ_5wCKFCgSl3vcqO_RKaSXbunuWIoSE", "Fisher & Paykel not draining"),
          V("164lrzpDHoRzS9UkwIlzo3k6y0z7_vmUt", "Upper water supply hose dropped"),
          D("1qEuq0doK2qSCWKhv3YhA158wyZvyxaFPITm1IaIOpJs", "Dishwasher cleaner"),
        ]},
        {"t": "If the issue persists, contact your Property Manager."},
      ],
    },
    {
      "q": "What should I do if the washing machine is not working?",
      "blocks": [
        {"t": "Check the power supply and record any error code. Refer to the manufacturer's manual for your model. You may restart the machine, check that the door is closed, redistribute an uneven load and clean an accessible filter as instructed in the manual. Do not disconnect hoses or remove fixed panels. Report any electrical, drainage or mechanical fault to your Property Manager."},
        {"media": [
          IMG("assets/img-laundry.jpg", "Laundry room diagram"),
          V("1gZ7EuWBbN5ZPP2b9ErOBNnLFzwRzMx0t", "Washing machine cleaning"),
          V("1ASLRslNYOCZ8NmpeFTQgoWc6W99qRb89", "No power? Troubleshooting"),
          V("1uo4m5SFIa1A0-8qp9tQuzNoE7i6zMwFM", "U-bend installation"),
          V("1qfqrjvO1rZsWNLQnXrzBw34b2DysZdLg", "Draining / filter cleaning"),
          V("1z7tjaUOePG0p2BEZ7dPLqEYn8AXrSnb3", "Door seal gap"),
        ]},
        {"t": "If the issue persists, contact your Property Manager."},
      ],
    },
    {
      "q": "What should I do if the dryer is not working?",
      "blocks": [
        {"t": "Check the power supply and record any error code. Refer to the manufacturer's manual for your model. You may check that the door is closed, reduce an overloaded drum, empty the water tank and clean accessible lint filters. Report drainage, electrical or mechanical faults to your Property Manager. Responsibility for the fault depends on its cause."},
        {"media": [
          P("1wpSqOSXvgzWKwaHOw7JQvMDw7t53Q5yI", "assets/cover-miele-dryer-06086650.png", "Miele dryer manual"),
          P("1yHWQ7s48-vQaUrQoS9z35WNJctMElNQW", "assets/cover-miele-dryer-manual.png", "Miele dryer user manual (English)"),
        ]},
      ],
    },
    {
      "q": "What should I do if the basin will not drain?",
      "blocks": [
        {"t": "Hair or soap residue may contribute to slow drainage. Remove only visible debris that can be reached safely, and do not dismantle the plumbing. Do not use chemical drain cleaner unless the product instructions, plumbing material and your Property Manager confirm that it is suitable. Never mix drain-cleaning products:"},
        {"media": [
          P("1eS0Tf8Zw1bi0DwT9hVaC0IhK2RSoplzX", "assets/cover-drainage.png", "Drain blockage guide"),
        ]},
        {"t": "Follow the approved product instructions exactly. Stop if you are unsure or if the basin is completely blocked, and contact your Property Manager."},
      ],
    },
    {
      "q": "What should I do if the toilet is leaking or will not flush?",
      "blocks": [
        {"t": "If water is actively leaking and the toilet isolation valve is accessible, turn it off only if you can do so safely. Do not force fittings or open a concealed cistern. Report the leak to your Property Manager immediately."},
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
      "q": "What should I do if a tap fitting is loose or the basin plug is stuck?",
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
        {"t": "Record any error code and contact your Property Manager. Contact building management only if the fault relates to a central building system and they have confirmed that they can reset it. Clean only an accessible filter in accordance with the approved guide:"},
        {"media": [
          V("1ndRNfxaL47Gd6fEthOzQwarDRC_TQTo_", "AC filter removal & cleaning"),
        ]},
      ],
    },
    {
      "q": "What should I do if the bed frame has collapsed?",
      "blocks": [
        {"t": "Stop using a collapsed or unstable bed frame and report it. Follow the video only for a minor adjustment where the frame is stable and no structural part is broken:"},
        {"media": [
          V("1ImyJ3kPlclJmEN_Th_kA8Ak_9-yrZKEc", "Bed frame repair"),
        ]},
        {"t": "If the issue persists, contact your Property Manager."},
      ],
    },
    {
      "q": "What should I do if the smoke alarm is not working or keeps beeping?",
      "blocks": [
        {"t": "Report any smoke alarm fault immediately. Do not remove, cover or disable the alarm. Replace a user-replaceable battery only if the alarm instructions and rental arrangements permit it; otherwise contact your Property Manager:"},
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
  "desc": "Lost keys, power outages, fire and urgent contacts",
  "questions": [
    {
      "q": "I have lost a key — what should I do?",
      "blocks": [
        {"t": "First, confirm whether you have lost the fob, which is the disc used for lift access, the physical key for your apartment door or the mailbox key."},
        {"t": "If you have lost a fob, contact your Property Manager for the current replacement process and a written breakdown of any charge. Check the number on the back of any remaining fob and verify all payment details through a trusted channel before paying."},
        {"t": "A lost apartment key may require replacement or rekeying for security. Contact your Property Manager for the available options and a written cost breakdown."},
        {"t": "If you have lost the mailbox key, contact your Property Manager for the current replacement process and confirmed cost."},
      ],
    },
    {
      "q": "What should I do during a power outage?",
      "blocks": [
        {"list": [
          "Check whether the outage affects only your apartment or the wider building",
          "If it is safe, check the switchboard for a tripped circuit",
          "Unplug the suspected appliance before making one reset attempt",
          "If it trips again, stop and report an urgent electrical fault; renters should contact their Property Manager and owners should contact a licensed electrician",
          "If there is a wider outage, contact your electricity distributor's outage service; check your electricity bill for the distributor's current number",
        ]},
      ],
    },
    {
      "q": "Fire & Emergency Evacuation",
      "blocks": [
        {"h": "Assembly Point"},
        {"t": "The building's nominated assembly point is currently the 【State Library Victoria forecourt】. Confirm this against the current evacuation diagram and follow any directions from wardens or emergency services."},
        {"t": "Use the signed emergency exit route shown on your floor's evacuation diagram."},
        {"h": "Lower & Mid-rise Residents (Levels 10–60)"},
        {"list": [
          "Do not search for the fire source or collect belongings during a fire alarm",
          "Check the door and handle with the back of your hand before opening",
          "Use the stairwell to access the fire stairs",
          "Do not use the lifts",
          "Follow the Fire Warden's instructions",
          "If you cannot evacuate safely, return to a safer enclosed location, close the door, call 000 and state your exact location",
          "Use the building emergency intercom or phone only where it is clearly identified on the evacuation diagram",
          "Do not re-enter the building until permitted",
        ]},
        {"h": "High-rise Residents (Levels 63–85)"},
        {"list": [
          "Do not use lifts during a fire unless a warden, firefighter or the building's emergency system expressly directs you to use a designated evacuation lift",
          "Follow the current evacuation diagram and emergency instructions for any designated refuge area",
          "Do not assume amenity rooms are refuge areas unless the current approved emergency plan identifies them as such",
          "If directed to a refuge area, remain there and follow instructions from wardens or emergency services",
        ]},
      ],
    },
    {
      "q": "Preventing False Alarms",
      "blocks": [
        {"list": [
          "Keep cooking appliances attended and use them only in their intended location. Do not obstruct, cover or alter smoke alarms, sprinklers, extinguishers or fire doors",
          "Do not cover smoke detectors",
          "Use the rangehood and appropriate ventilation while cooking. If there is an uncontrolled fire or dangerous smoke, leave the area, close the door if safe and call 000",
          "Familiarise yourself with the fire plan and evacuation routes in advance",
        ]},
        {"h": "Smoke Alarms Inside Apartments"},
        {"list": [
          "Smoke alarm locations and types vary between apartments",
          "Do not assume an apartment smoke alarm will automatically notify building management or emergency services",
          "Treat every alarm as genuine until you have safely confirmed otherwise, and follow the building's emergency instructions",
          "Respond to any alarm promptly",
          "Do not cover or remove the detector",
        ]},
        {"h": "Common-area Sounders"},
        {"t": "Some building alarms may automatically notify emergency services; do not rely on this. Call 000 if you see fire or smoke or believe anyone is in danger. When an alarm sounds, follow the emergency announcement. Before opening your apartment door, check for heat or smoke and do not open it if it is unsafe."},
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
        {"t": "First use your Property Manager's urgent-repair contact. If you cannot obtain a prompt response, follow the current Victorian urgent-repair process before engaging a tradesperson. Use the contacts below only for urgent matters, keep invoices and receipts, and confirm who is responsible for the cost. A lockout is an emergency access issue but is not necessarily a statutory urgent repair."},
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
  "title": "Rental Agreement Changes, Transfers & Early Termination",
  "desc": "Renewals, housemates, transfers, subletting and early termination",
  "questions": [
    {
      "q": "My rental agreement is expiring — can I renew it?",
      "blocks": [
        {"t": "Generally, if the rental provider has no other plans and you have looked after the property well, caused no damage and kept it clean and tidy, you may renew the rental agreement for either 12 months or 6 months. Please contact your Property Manager to discuss the available options."},
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
        {"t": "You may advertise on social media yourself, or ask us to advertise the property through platforms such as realestate.com.au and Domain. The advertising fee is a one-off payment of $330, payable in advance to O REAL (BSB 733003, Acc 727393)."},
        {"t": "Please note that paying the advertising fee does not guarantee that we will find a replacement renter. The outgoing renter remains responsible for rent and any related costs until the new rental agreement begins or the existing rental agreement otherwise legally ends."},
      ],
    },
    {
      "q": "I have found someone to take over the rental agreement — what happens next?",
      "blocks": [
        {"t": "Ask your Property Manager how the proposed renter should apply through the approved secure process. If the application is approved, the Property Manager will confirm whether the arrangement is a transfer, change of renter or sublet, and provide the required documents, RTBA bond steps, effective date and an itemised explanation of any lawful costs."},
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
        {"t": "Your Property Manager will send you a vacate guide explaining the required condition and optional cleaning arrangements. You may choose your own cleaner; using an agency-recommended cleaner is not required. You must return the property in a reasonably clean condition, taking into account its condition at the start of the rental agreement. Stains or damage will be assessed against the condition report, the property's age and condition, fair wear and tear, and the cause. Professional cleaning can only be required where permitted by the rental agreement and Victorian law and where reasonably necessary."},
        {"t": "Keep electricity connected until the agreed handover or inspection date if reasonably required and confirmed in advance. Arrange disconnection for an agreed date so that you are not charged beyond your responsibility."},
        {"t": "We aim to complete the 【exit inspection】 promptly after the keys are returned and will notify you of any concerns. If your cleaner provided a written return-to-clean guarantee, contact the cleaner about eligible cleaning concerns. Other claims will be assessed separately, with evidence and allowance for fair wear and tear."},
        {"t": "A responsibility or bond-transfer form is required only where the rental agreement is being transferred or the renters are changing. It is not part of every move-out."},
        {"t": "A bond claim can be initiated through the RTBA after the rental agreement ends. The parties may agree on how the bond is paid; disputed claims follow the RTBA and VCAT process. Follow the RTBA's official instructions and verify that any email or link is genuine before entering bank details. The move-out process is complete once the keys are returned, outstanding matters are finalised and the bond process has been completed."},
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
