import pywhatkit

text = "1. Apa yang dimaksud dengan swarm intelligence? \nJawab: Swarm intelligence adalah disiplin keilmuan yang berhubungan dengan sistem alami dan buatan, dimana terdiri dari banyak individu atau populasi yang berkoordinasi menggunakan konsep control desentralisasi dan self organized. \n2. Apa yang menjadi karakteristik atau keunikan dari algoritma swarm intelligence dibandingkan algoritma lainnya? \nJawab: Karakteristik algoritma swarm intelligence itu adalah: \na)Membuat design ulang representasi solusi \nb)Beberapa dari mekanisme alami belum dipahami \nc)Terkadang tidak mencapai solusi global optimal atau mengalami kegagalan dimana terjebak pada local optimal \nd)Setiap problem optimasi yang akan diselesaikan"

pywhatkit.text_to_handwriting(text, rgb=(0, 0, 0)) #using rgb to make the handwriting black color
