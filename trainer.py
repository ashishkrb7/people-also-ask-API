import pickle
import src
data=["Could you give please?","Do you think you could lend me some money?",
"I wonder whether you could give me a car.","I am sorry to trouble you but I need your help.",
"I hope you don't mind if l asked the money.","Would you mind if I ask your help?","I request you to grant me leave.",
"How about giving your car please?","Kindly allow me to talk.",
"Please let me know if you come or not.","Could you open the door for me, please?",
"Would you mind opening the door for me, please?","Can you open the door for me, please?",
"Can I use your computer, please?","Could I borrow some money from you, please?","Do you mind if I turn up the heating?",
"Would you mind if I turned up the heating?","Speaking tip: Could is more polite that can",
"Can I help you?","Shall I open the window for you?","Would you like another coffee?","Would you like me to answer the phone?",
"I’ll do the photocopying, if you like.","Shall, can and will are followed by the verb without to.","Do me a favour, will you?",
"Would it be possible for you to?","Can I ask you to?"
]

src.dumptrain(data,"Request")