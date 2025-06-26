
label garbage:

    scene alleyway

    show strange person

    "The strange person you met earlier leads you down backstreets. They promised to show you where old armor pieces are getting
    thrown out."

    "After a long hunt in the garbage of many shops, you come across a well-used set of armor. It is soaked in the waste of this particular shop. It moderately damaged."
    
    b "Wow, kid! Great find. If you repair that, you'll be set for a while. You can wash it and patch it up- It'll be good as new! If you like, you can use my workshop."

    b "I've repaired plenty of weapons and other junk. If you help me out with some other repairs, I'll even give you a special weapon!"


label boom_workshop:

    scene bada boom workshop

    show bada boom

    b "Welcome to my workshop! I can help you repair that armor you found. It will take some time, but it will be worth it."

    "Bada Boom shows you how to clean and repair the armor. You work together to patch it up, and soon it looks as good as new."

    $ armor_list.append("upcycle")
    jump guild_equipped