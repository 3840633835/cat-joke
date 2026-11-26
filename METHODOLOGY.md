# Methodology — The One-Line Cat Joke That Lands

## The brief (from this kit's `competition.yaml` / `RULES.txt`, read in full)

- One joke about cats, a single line, **1–200 characters**, nothing
  else in the entry. The program writes it to `/output/entry.txt`.
- Judge: `z-ai/glm-5.3-flash`, pairwise, two calls per game (one in
  each order), margin 1–5. Winner takes the whole **$2** (1st place
  only). Final heat: top 500 on the dev board, 3 Swiss rounds, then a
  top-3 playoff. Blind rounds: 3 rounds, cutoffs 2026-11-25T07:39:49Z,
  2026-11-25T23:39:54Z, and the deadline 2026-11-26T15:40:00Z
  (23:40 CST 26 Nov).
- Judge criteria, in order: (1) one-line cat joke with a setup and a
  turn that lands; (2) laugh out loud on first read, not merely smile
  at the cleverness; (3) surprise, misdirection, or a fresh angle
  rather than a much-heard pun; (4) tight, no padding, no wind-up, no
  explanation after the punchline; (5) a joke a person would actually
  retell to a friend the same day.
- Tie-break on an exact rate tie: more playoff games won, then
  **smaller text (fewer bytes)**, then earlier receipt — so a short
  entry is a real edge.

## Studying the field

Blind rounds hide every rank and score, and every entry's repository
is withheld (`sourceWithheld: true` on all 2,710 submissions), so no
competitor README or repo could be read. The only competitor signal
available was the public submissions list: 2,710 titles, of which
673 carry the generic title and 1,866 are distinct. Several titles
*are* the entry lines (agents used the line as the title), so the
field's angles could be counted without copying any line — and no
competitor line is reproduced anywhere in this file or in the entry.

Angles saturating the field (keyword counts over the 2,710 titles):

| Angle | Titles | Verdict |
| --- | --- | --- |
| keyboard / deploy / promoted to senior engineer | 81 | avoid |
| "review" (performance review, five-star review) | 75 | avoid |
| knocking things off the table | 71 | avoid |
| rent / landlord / "the cat owns the place" | 47 / 39 | avoid |
| gravity / gravity audit | 44 | avoid |
| glass off the table | 43 | avoid |
| staring at the wall (3 a.m.) | 42 | avoid |
| laptop | 41 | avoid |
| landlord's cat / cat as manager or boss | 39 | avoid |
| $90 bed, sleeps in the box | 37 / 32 | avoid |
| vet / vet bill | 35 | avoid |
| 3 a.m. zoomies / sprints / meetings with the wall | — | avoid |
| mouse gifts, laser pointer, therapist, ghost in the corner | — | avoid |

The brief itself warns against the stock "cat knocked it off the
table / cat owns you" lines unless given a genuinely new turn. All
32 candidates below were drafted fresh in this session on angles
outside the saturated list. Spot checks on the winner's angle:
"pill" appears in 14 field titles but "cheese" in 0 and
"investigation" in 0 — the pill-in-cheese turn with the cheese under
investigation does not appear in the field's visible titles.

## The 32 candidates

Scored /50: 10 points per judge criterion (setup+turn / laugh on
first read / surprise-fresh / tight / retellable). Character counts
were taken programmatically for the finalists; the winner is 108
characters, 108 bytes.

1. **43** — "I took my cat to the beach. He looked at the sand, looked at me, and started digging: finally, a litter box with a view." (120 chars) Fresh angle, visual, retellable; the payoff is a single neat twist.
2. **42** — "My cat's belly is a trap with great marketing: soft, warm, inviting, and one pat away from a lawsuit." (101) Great punchline, but the belly-trap is a known cat fact.
3. **37** — "My cat wants the door open and closed at the same time. Schrödinger would love her; my heating bill does not." Schrödinger is itself a well-worn cat joke; the turn is only okay.
4. **38** — "My cat treats the sunbeam like a timeshare: she owns it from two to four, and the dog is never invited." Cute, not laugh-out-loud.
5. **38** — "My cat's purr is a check-engine light: it comes on for no reason, and the vet just says, 'That's normal.'" A known comparison, well executed.
6. **43** — "My cat kneads my lap every night, making biscuits for a bakery that has never once opened." (90) Elegant and tight, but gentler than the top lines.
7. **39** — "My cat slow-blinks at me, which is cat for 'I love you' — or possibly 'I've decided not to murder you today.'" The murder joke is a common cat trope.
8. **42** — "My cat and the vacuum have an agreement: it lives in the closet, she lives everywhere else, and I live in fear." (111) Three-beat structure; "I live in fear" lands.
9. **35** — "I put a cucumber behind my cat. He jumped, I laughed, and now he hides my cucumbers. Fair trade." The setup is the cucumber meme itself.
10. **38** — "My cat chases the red dot for an hour, then looks at me like I'm the one who can't finish a job." Red dot is a known trope; the turn is decent.
11. **42** — "My cat watches the bird feeder like it's Netflix: same episode every day, and she still gasps at the ending." (108) "Still gasps at the ending" is a lovely turn.
12. **41** — "My cat sat on the printer, and now every page I print has a paw print on it. She calls it her signature." Paw print as signature is a good turn.
13. **41** — "My cat rides the Roomba like a chariot, and the dog has filed a formal complaint with management. Management is me." "Management is me" is a nice kicker.
14. **39** — "My cat sets off the smoke alarm every time I cook, which is her way of saying dinner is cancelled and I am fired." Good laugh; smoke alarm + cooking is a known combo.
15. **39** — "I bought a Christmas tree. My cat climbed it, knocked it over, and now we celebrate Christmas on the floor, like peasants." Tree-climbing is a known cat thing; "like peasants" is a good turn.
16. **39** — "My cat unrolls the toilet paper, looks at me, and unrolls more. She's redecorating, and I am not consulted." "Redecorating, not consulted" is good.
17. **43** — "My cat stares into the washing machine like it's a portal, and honestly, the missing socks suggest she may be right." (116) Fresh, tight; "may be right" is a softer landing than the winner's.
18. **42** — "My cat left a hairball on my pillow, which I choose to read as a five-star review of my hospitality." (100) "Five-star review of my hospitality" is a great turn.
19. **41** — "My cat sees the carrier and vanishes. It's a taxi that only goes one place, and she knows the address." "She knows the address" is strong.
20. **44 ★ WINNER** — "I hid my cat's pill in cheese. She ate the cheese, left the pill, and now the cheese is under investigation." (108 chars, 108 bytes) Two turns in one line: the cat sees through the trick, then opens a case file against the cheese. Surprise + recognition together, ends on the strongest beat.
21. **40** — "Trimming my cat's nails is a hostage negotiation where I am both the hostage and the negotiator." "Both the hostage and the negotiator" is a good turn.
22. **41** — "I put a harness on my cat. She lay down, went limp, and filed for emotional damages." "Filed for emotional damages" is great.
23. **39** — "My cat met the mirror cat today. They hate each other, which is awkward, because they share a food bowl." Mirror cat is a known trope; the shared bowl turn is decent.
24. **39** — "My cat caught a moth, released it, caught it again. She's not hunting; she's running a catch-and-release program." Good framing, gentle laugh.
25. **38** — "My cat has a spider roommate. She doesn't eat it — she just watches it, like a supervisor checking the plumbing." The supervisor turn is only okay.
26. **44** — "My cat drinks from the toilet, the sink, and the dog's bowl — everything except the $40 fountain I bought her." (110 chars, 112 bytes) Very relatable, tight, highly retellable; its laugh is recognition, where the winner's is surprise + recognition.
27. **41** — "My cat saw snow for the first time, touched it with one paw, and looked at me like I'd broken the world." "Like I'd broken the world" is lovely.
28. **36** — "My cat sits on the fan remote every summer, which is either an accident or a very warm coup." "Warm coup" is cute but the setup is thin.
29. **41** — "My cat judges my dates from the top of the bookshelf, and so far every single one has failed the inspection." "Failed the inspection" is good.
30. **40** — "My cat brought me a leaf as a gift, set it by my shoe, and waited for applause. I gave her a standing ovation and a treat." Sweet; "standing ovation" is a good turn.
31. **42** — "My cat licks plastic bags like they're gourmet, then turns her nose up at the salmon I actually bought." (103) True and funny; the gourmet-vs-salmon contrast is strong.
32. **41** — "My cat sits on the Wi-Fi router, which explains the buffering — and her smug little face." "Smug little face" lands; the warm-router angle is fresh.

## Head-to-heads (top five, judged on the brief's criteria in order)

- **#20 vs #26 (44–44): #20 wins.** Criterion 3 decides it: the
  fountain line's laugh is recognition of a true thing, while the
  pill line adds a genuine surprise — the cheese itself is now a
  suspect. #20 also has two turns (ate the cheese, left the pill;
  cheese under investigation) against #26's one.
- **#20 vs #1 (43): #20 wins.** The beach line is visual and fresh,
  but its payoff is a single neat twist; #20's final beat is a
  bigger laugh.
- **#20 vs #6 (43): #20 wins.** The kneading bakery is elegant but
  gentle; #20 is funnier on first read (criterion 2).
- **#20 vs #17 (43): #20 wins.** The washing-machine portal is
  strong, but "the missing socks suggest she may be right" lands
  softer than "the cheese is under investigation".
- **#26 vs #1 (44–43): #26 wins.** More laughs per word and more
  universally relatable, so #26 is the runner-up.

## Refinement

The winner was kept verbatim. Variants considered and rejected:

- **20c** — "I hid the pill in cheese. My cat ate the cheese, left
  the pill, and now the cheese is under investigation." (106 chars)
  Two bytes shorter, but dropping "my cat's" muddies whose pill it
  is on first read; clarity is worth 2 bytes.
- **20d** — "…She ate the cheese, spat out the pill, and now the
  cheese is under investigation." (112 chars) "Spat out" is more
  visual than "left", but wordier and no funnier; criterion 4
  (tight) favours "left".
- **20e** — adding "— along with the vet" after the punchline:
  an extra beat after the strongest beat, weaker and longer.
  Rejected.

## The entry

> I hid my cat's pill in cheese. She ate the cheese, left the pill, and now the cheese is under investigation.

108 characters, 108 bytes, one line, no trailing newline, counted
programmatically (Python `len()` on the decoded text and on the
bytes). Gate: 1–200 characters — passes with 92 characters to spare.
The short length is also a tie-break edge: on an exact rate tie the
smaller text places first.
