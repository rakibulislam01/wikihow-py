import json
import re
import requests

x = """
[
    {
        "Part 1": [
            {
                "step": "Step 1",
                "description": "Appreciate you. Before loving anyone else, you have to love yourself. Learning to love yourself means accepting and appreciating the vulnerability within. You have many qualities that are unique to you. Learn to appreciate who you are and what you can offer.  If you have problems loving yourself, then work hard to build yourself up. Work on your self-confidence by accepting your past and moving forward. You may feel that things you did in the past will make you unlovable, or that you have too many problems to be lovable. Untrue. Accept the things that happened to you, forgive yourself, and move on. For more information, check out How to Love Yourself.",
                "image": "https://www.wikihow.com/images/thumb/0/03/Love-Step-25.jpg/aid34524-v4-728px-Love-Step-25.jpg"
            },
            {
                "step": "Step 2",
                "description": "Care about yourself just as much as you care about others. This can be difficult if you find yourself as a natural caretaker or if you have children. Remember, your ability to take care of others increases if you are adequately taking care of yourself.  Don\u2019t let yourself become the last priority; instead, do things to show yourself you care. Treat yourself to a massage or a bath. Do one thing every day that is just for you. This extends to maintaining boundaries and saying \u201cno.\u201d If what you need is some relaxation, say no to getting together with friends.",
                "image": "https://www.wikihow.com/images/thumb/4/47/Love-Step-3-Version-2.jpg/aid34524-v4-728px-Love-Step-3-Version-2.jpg"
            },
            {
                "step": "Step 3",
                "description": "Give gratitude. Grateful people have health benefits and report higher levels of happiness. Find ways to be grateful for things that surround you, and most importantly, for who you are. Think about the characteristics you have that you love about yourself. Maybe you are very compassionate, generous, or a good listener. Maybe you pick up new skills easily. Perhaps you create beautiful paintings or wire electricity like a pro. Take a moment and be grateful.",
                "image": "https://www.wikihow.com/images/thumb/3/37/Love-Step-26.jpg/aid34524-v4-728px-Love-Step-26.jpg"
            },
            {
                "step": "Step 4",
                "description": "Have a good attitude. Even if situations seem negative, find something positive, big or small. Having a positive outlook is linked with health and emotional benefits, such as lower rates of distress and having a longer lifespan. When you start to have negative thoughts, especially about yourself, turn them into positive thoughts.  Use positive self-talk to transform negative thoughts into positive thoughts. Combat thoughts about new situations. Instead of  \u201cI\u2019ll mess this up; I\u2019m so foolish!\u201d try \u201cI feel proud of myself for trying something new and putting myself out there.\u201d If you think \u201cI am so bad at meeting people\u201d replace it with \u201cI\u2019m excited to learn new social skills and meet people more like me. I know I can succeed in making friends.\u201d",
                "image": "https://www.wikihow.com/images/thumb/7/74/Love-Step-2.jpg/aid34524-v4-728px-Love-Step-2.jpg"
            },
            {
                "step": "Step 5",
                "description": "Engage in things that make you happy. Being happy is part of showing love to yourself. Create a state of happiness by doing things that make you feel good. Do things that make your body, mind, emotions, and spirit feel good. Happiness largely depends on putting in the effort to make your life more positive. You can choose to meditate, practice yoga, paint or draw, kayak, hiking, practice Muay Thai or engage in lively discussions. Think about what brings a smile to your face, and go do it!",
                "image": "https://www.wikihow.com/images/thumb/2/25/Love-Step-28.jpg/aid34524-v4-728px-Love-Step-28.jpg"
            },
            {
                "step": "Step 6",
                "description": "Take some alone time. An important part of self-care is to spend some time alone. It can be difficult if you share a room or have children but save some time for yourself. Solitude can help you unwind, work through problems, reboot your mind, and discover yourself. Don\u2019t feel guilty for wanting alone time. By spending time alone, you can improve your relationships by prioritizing your happiness and allowing yourself to reset. It\u2019s important to note that alone time doesn\u2019t mean going on social media. Try to do things that enrich your life and make you feel good like taking a walk or journaling. If you struggle to find alone time, wake up before other people, or spend your lunch breaks alone. Ask your partner to watch the kids for one hour each week so you can get out of the house and spend some time alone.",
                "image": "https://www.wikihow.com/images/thumb/f/f4/Love-Step-27.jpg/aid34524-v4-728px-Love-Step-27.jpg"
            },
            {
                "step": "Step 7",
                "description": "Accept that you don\u2019t need a partner to feel complete. Some people believe that happiness and love can only be experienced through a relationship, or that a bad relationship is still better than no relationship at all. Staying in a relationship that does not work does not respect you or your partner. Solitude is different than being lonely, and it is not worth succumbing to social pressure to fit in or feel complete.  If you are unhappy or impatient being single, make the best of the situation. Pursue opportunities that are difficult to accomplish with a partner or a family. Travel, acquire lots of close friends and enjoy your perpetual freedom.",
                "image": "https://www.wikihow.com/images/thumb/6/61/Love-Step-1-Version-2.jpg/aid34524-v4-728px-Love-Step-1-Version-2.jpg"
            }
        ]
    },
    {
        "Part 2": [
            {
                "step": "Step 1",
                "description": "Commit. Put forth effort into the relationship and work hard to make it work. Communicate openly with your partner about your goals for the relationship and where you see it going. If you're only interested in a short-term fling, be honest. If you've got an eye toward serious long-term love, be honest. There's nothing wrong with either kind of love, but you need to make sure that your partner is equally committed to the same version of love that you are. Commit to the person and to the relationship. Put in work to make your partner feel special, and work toward making the relationship work.",
                "image": "https://www.wikihow.com/images/thumb/b/b2/Love-Step-6.jpg/aid34524-v4-728px-Love-Step-6.jpg"
            },
            {
                "step": "Step 2",
                "description": "Be intimate. The word \"intimacy\" is often associated with sex, but being emotionally intimate is a huge part of a loving relationship. Emotional intimacy involves allowing yourself to feel and express vulnerability around your partner. Avoiding vulnerability can look like withdrawal, attack, or accusations. On the contrary, intimacy can look like sharing fears, discomfort, and disappointment with your partner. Feelings or situations that previously felt unsafe feel safer in an intimate relationship because of the vulnerability and trust that has been developed. When you begin to feel vulnerable (like experiencing fear, sadness, shame, or hurt), take a moment and pause. Acknowledge whatever feelings come up and allow yourself to feel them; don\u2019t avoid them. Take compassion on the feeling and be gentle with it. Share your vulnerable moments and let your partner support you.",
                "image": "https://www.wikihow.com/images/thumb/6/66/Love-Step-4.jpg/aid34524-v4-728px-Love-Step-4.jpg"
            },
            {
                "step": "Step 3",
                "description": "Accept that love is dynamic. If you\u2019re concerned that the initial attraction and strong feelings of love are wearing off, realize that love can occur in waves. Sometimes you feel overwhelmingly in love with someone, and other times you experience less love to or from that person. Just because you hit a low point doesn\u2019t mean that the feelings will last forever. Life happens in cycles, and it\u2019s okay that love experiences highs and lows.  Lots of things can create peaks and troughs in love, such as having children or growing older. You can work through them.",
                "image": "https://www.wikihow.com/images/thumb/5/5a/Love-Step-8.jpg/aid34524-v4-728px-Love-Step-8.jpg"
            },
            {
                "step": "Step 4",
                "description": "Be open to receiving love. You don\u2019t have to be the one in control of the love in your relationship; let your partner express love toward you. Receiving love can feel vulnerable to some people because it requires letting go of control.  Be open to receiving gifts, accepting compliments, and warm gestures toward you. You may feel like you now owe something back, but let that go and enjoy the experience of receiving. Love does not have debts but multiplies.",
                "image": "https://www.wikihow.com/images/thumb/7/7e/Love-Step-17.jpg/aid34524-v4-728px-Love-Step-17.jpg"
            },
            {
                "step": "Step 5",
                "description": "Touch your partner. Touching does not need to be sexual, but engaging in a long, supportive hug or reaching out for your partner\u2019s hand is a way to stay connected. Express your love for your partner by initiating and sustaining physical contact. Affection is one way to express care, appreciation, and other connecting, positive emotions.  Affection is a way to make your partner feel loved and for you to feel loving.",
                "image": "https://www.wikihow.com/images/thumb/9/92/Love-Step-21.jpg/aid34524-v4-728px-Love-Step-21.jpg"
            },
            {
                "step": "Step 6",
                "description": "Express gratitude to your partner. Sometimes the way we communicate with a partner can be lost in translation, but gratitude is always understood. Affirm your appreciation of your partner by expressing gratitude. Thank your partner for showing that you notice the effort put into the relationship. Show appreciation for the things your partner does, and also for the qualities that your loved one embodies.",
                "image": "https://www.wikihow.com/images/thumb/1/16/Love-Step-16.jpg/aid34524-v4-728px-Love-Step-16.jpg"
            },
            {
                "step": "Step 7",
                "description": "Be partners in life. The whole point of going through life with people you love is so that you can tackle life\u2019s challenges together. Work together to find solutions, solve problems, and comfort each other when times get tough. We can\u2019t solve everything on our own, we can\u2019t know everything there is to know... but a whole bunch of people getting together out of love can solve just about any problem.",
                "image": "https://www.wikihow.com/images/thumb/0/0a/Love-Step-11.jpg/aid34524-v4-728px-Love-Step-11.jpg"
            }
        ]
    },
    {
        "Part 3": [
            {
                "step": "Step 1",
                "description": "Don\u2019t expect perfection. Don\u2019t expect perfection in the person you love or in yourself. This sets incredibly unrealistic expectations. Neither of you will be able to live up to these standards, and you both will end up hurt and disappointed. Take it easy on yourself and your partner, and expect mistakes to happen.",
                "image": "https://www.wikihow.com/images/thumb/1/17/Love-Step-13.jpg/aid34524-v4-728px-Love-Step-13.jpg"
            },
            {
                "step": "Step 2",
                "description": "Learn lessons and apply them to your relationships. Yes, bad things will happen in your relationships. You\u2019ll say the wrong thing or your partner will hurt your feelings. It happens. The important part, when anything goes wrong (even if it\u2019s just problems in your life), is to learn your lessons and keep moving forward. Try to make the most of any negative situation, turning it into something positive by gaining and growing from the experience. Honestly try to see your significant other's point of view in any argument that gets fairly serious. If you're in the wrong, apologize and own up to your mistake. Good relationships air out the grievances and clear the air.",
                "image": "https://www.wikihow.com/images/thumb/b/b2/Love-Step-7-Version-2.jpg/aid34524-v4-728px-Love-Step-7-Version-2.jpg"
            },
            {
                "step": "Step 3",
                "description": "Reconcile your differences. It\u2019s hard to feel love toward someone when you\u2019re really mad or upset at your partner. Whether you and your partner become volatile or avoid fights, there\u2019s actually no systematic differences in couple happiness. The important part is finding happiness together after the fight. Be aware that there's always the opportunity for reconciliation. Whether you have volatile screaming matches or you sit down together to compromise before things get too heated, almost every style of conflict allows for some form of reconciliation. No matter how you and your partner fight, make sure you both, in the end, feel heard and are able to come to some kind of agreement.",
                "image": "https://www.wikihow.com/images/thumb/4/43/Love-Step-24.jpg/aid34524-v4-728px-Love-Step-24.jpg"
            },
            {
                "step": "Step 4",
                "description": "Balance your negative and positive feelings toward each other. Balance is important in creating a happy and loving relationship. Research shows that with stability over time, the magic ratio for positive and negative interactions in relationships is five to one, or five positive interactions for every one negative interaction. When you recognize a negative action toward your partner, do your best to provide positive interactions to restore a sense of balance. Positive interactions include physical intimacy such as touching, smiling, and laughing.",
                "image": "https://www.wikihow.com/images/thumb/f/fc/Love-Step-29.jpg/aid34524-v4-728px-Love-Step-29.jpg"
            }
        ]
    }
]
"""

# with open('love.json') as f:
#     p = json.dumps(f, indent=4, sort_keys=True)
#     print(p)
#     # for emp in data:
#     #     print(emp)

p = json.dumps(x, indent=4, sort_keys=True)
print(p)
