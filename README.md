CLTK Latin sentence tokenizer
=============================

About
-----

Training sets and and sentence tokenizer for Classical Greek, for use with [Classical Language Toolkit](https://github.com/kylepjohnson/cltk). Unless you are a CLTK developer, there is nothing you need from this repository. The main file here is `greek.pickle`, which you [import according to the docs here](http://docs.cltk.org/en/latest/import_corpora.html).

Use
---

For instructions on tokenizing sentences, see [instructions in the CLTK docs](http://docs.cltk.org/en/latest/classical_latin.html#sentence-tokenization).

To create a new training set (steps #1 and 2), do the following within this repository's root directory. Use steps #3 and 4 to test the output.

```python
In [1]: from sentence_tokenizer import train_from_file

In [2]: train_from_file('training_sentences.txt')
  Abbreviation: [0.3255] ἐᾶν
  Abbreviation: [0.3255] ἔζη
  Abbreviation: [0.8848] ὄν
  Sent Starter: [366.4722] 'ὁ'
  Sent Starter: [32.3856] 'καίτοι'
  Sent Starter: [54.1370] 'οὐκοῦν'
  Sent Starter: [338.3707] 'ἐνταῦθα'
  Sent Starter: [127.1078] 'ἐκ'
  Sent Starter: [59.5778] 'ἀκούσασ'
  Sent Starter: [653.2848] 'ἐπεὶ'
  Sent Starter: [45.2915] 'ταύτην'
  Sent Starter: [66.8957] 'εἰ'
  Sent Starter: [47.9663] 'ἀκούσαντεσ'
  Sent Starter: [230.3898] 'καὶ'
  Sent Starter: [432.8013] 'ἐντεῦθεν'
  Sent Starter: [32.3856] 'τοιγαροῦν'
  Sent Starter: [98.9058] 'ἐπειδὴ'
  Sent Starter: [116.9693] 'οἱ'
  Sent Starter: [103.8642] 'ἔνθα'
  Sent Starter: [58.9851] 'ταῦτα'
  Sent Starter: [36.9662] 'ἀλλὰ'
  Sent Starter: [187.9368] 'μετὰ'

In [3]: from sentence_tokenizer import tokenize_sentences

In [4]: tokenize_sentences('models/xen_anab_1.txt')
['Δαρείου καὶ Παρυσάτιδος γίγνονται παῖδες δύο, πρεσβύτερος μὲν Ἀρταξέρξης, νεώτερος δὲ Κῦρος: ἐπεὶ δὲ ἠσθένει Δαρεῖος καὶ ὑπώπτευε τελευτὴν τοῦ βίου, ἐβούλετο τὼ παῖδε ἀμφοτέρω παρεῖναι.', 'ὁ μὲν οὖν πρεσβύτερος παρὼν ἐτύγχανε: Κῦρον δὲ μεταπέμπεται ἀπὸ τῆς ἀρχῆς ἧς αὐτὸν σατράπην ἐποίησε, καὶ στρατηγὸν δὲ αὐτὸν ἀπέδειξε πάντων ὅσοι ἐς Καστωλοῦ πεδίον ἁθροίζονται.', 'ἀναβαίνει οὖν ὁ Κῦρος λαβὼν Τισσαφέρνην ὡς φίλον, καὶ τῶν Ἑλλήνων ἔχων ὁπλίτας ἀνέβη τριακοσίους, ἄρχοντα δὲ αὐτῶν Ξενίαν Παρράσιον.', 'ἐπεὶ δὲ ἐτελεύτησε Δαρεῖος καὶ κατέστη εἰς τὴν βασιλείαν Ἀρταξέρξης, Τισσαφέρνης διαβάλλει τὸν Κῦρον πρὸς τὸν ἀδελφὸν ὡς ἐπιβουλεύοι αὐτῷ.', 'ὁ δὲ πείθεται καὶ συλλαμβάνει Κῦρον ὡς ἀποκτενῶν: ἡ δὲ μήτηρ ἐξαιτησαμένη αὐτὸν ἀποπέμπει πάλιν ἐπὶ τὴν ἀρχήν.', 'ὁ δ᾽ ὡς ἀπῆλθε κινδυνεύσας καὶ ἀτιμασθείς, βουλεύεται ὅπως μήποτε ἔτι ἔσται ἐπὶ τῷ ἀδελφῷ, ἀλλά, ἢν δύνηται, βασιλεύσει ἀντ᾽ ἐκείνου.', 'Παρύσατις μὲν δὴ ἡ μήτηρ ὑπῆρχε τῷ Κύρῳ, φιλοῦσα αὐτὸν μᾶλλον ἢ τὸν βασιλεύοντα Ἀρταξέρξην.', 'ὅστις δ᾽ ἀφικνεῖτο τῶν παρὰ βασιλέως πρὸς αὐτὸν πάντας οὕτω διατιθεὶς ἀπεπέμπετο ὥστε αὐτῷ μᾶλλον φίλους εἶναι ἢ βασιλεῖ.', 'καὶ τῶν παρ᾽ ἑαυτῷ δὲ βαρβάρων ἐπεμελεῖτο ὡς πολεμεῖν τε ἱκανοὶ εἴησαν καὶ εὐνοϊκῶς ἔχοιεν αὐτῷ.', 'τὴν δὲ Ἑλληνικὴν δύναμιν ἥθροιζεν ὡς μάλιστα ἐδύνατο ἐπικρυπτόμενος, ὅπως ὅτι ἀπαρασκευότατον λάβοι βασιλέα.', 'ὧδε οὖν ἐποιεῖτο τὴν συλλογήν.', 'ὁπόσας εἶχε φυλακὰς ἐν ταῖς πόλεσι παρήγγειλε τοῖς φρουράρχοις ἑκάστοις λαμβάνειν ἄνδρας Πελοποννησίους ὅτι πλείστους καὶ βελτίστους, ὡς ἐπιβουλεύοντος Τισσαφέρνους ταῖς πόλεσι.', 'καὶ γὰρ ἦσαν αἱ Ἰωνικαὶ πόλεις Τισσαφέρνους τὸ ἀρχαῖον ἐκ βασιλέως δεδομέναι, τότε δὲ ἀφειστήκεσαν πρὸς Κῦρον πᾶσαι πλὴν Μιλήτου: ἐν Μιλήτῳ δὲ Τισσαφέρνης προαισθόμενος τὰ αὐτὰ ταῦτα βουλευομένους ἀποστῆναι πρὸς Κῦρον, τοὺς μὲν αὐτῶν ἀπέκτεινε τοὺς δ᾽ ἐξέβαλεν.', 'ὁ δὲ Κῦρος ὑπολαβὼν τοὺς φεύγοντας συλλέξας στράτευμα ἐπολιόρκει Μίλητον καὶ κατὰ γῆν καὶ κατὰ θάλατταν καὶ ἐπειρᾶτο κατάγειν τοὺς ἐκπεπτωκότας.', 'καὶ αὕτη αὖ ἄλλη πρόφασις ἦν αὐτῷ τοῦ ἁθροίζειν στράτευμα.',
```

Now that you have a customized `latin.pickle`, you may copy it to your local CLTK data directory at `~/cltk_data/compiled/sentence_tokens_latin/`. If you think your tokenizer is an improvement upon the CLTK's current, please submit a pull request along with the original training set.


Contents
--------

`greek.pickle`: the actual sentence tokenizer

`greek.tar.gz`: this is `latin.pickle` and `training_sentences.txt` compressed; what is fetched by the CLTK corpus importer

`models/`: original texts and training sentences

`sentence_tokenizer.py`: a script which generates `greek.pickle`

`tokenized_output.txt`: example output from the trainer.

`training_sentences.txt`: the combined output of the training sentences in `models`

`transformer.py`: a quick and dirty script with which I cleaned up Cicero's *Catalinarians* (12,236 words) into `training_sentences.txt`. In it, each sentences starts a new line


