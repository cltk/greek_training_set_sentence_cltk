CLTK Greek sentence tokenizer
=============================

About
-----
Training sets and sentence tokenizer for Classical Greek, for use with the [Classical Language Toolkit](https://github.com/kylepjohnson/cltk). Unless you want to create a new training set for Greek sentences, there is nothing you need from this repository.

To tokenize Greek sentences with the CLTK, first [import it and use according to the docs here](http://docs.cltk.org/en/latest/import_corpora.html) and then see [instructions on tokenizing Greek sentences](http://docs.cltk.org/en/latest/classical_greek.html#sentence-tokenization).

Use
---
To create a new training set, manually add tokenized sentences (with each sentence starting a new line) to `training_sentences.txt` and run `train_sentence_tokenizer.py`. The script outputs `greek.pickle`. To use this new file, copy it to your local CLTK data directory at `~/cltk_data/compiled/sentence_tokens_greek/`. If you think your training set and tokenizer is an improvement over the CLTK's current, please submit a pull request.

```shell
$ python train_sentence_tokenizer.py 
  Abbreviation: [0.3233] ἐᾶν
  Abbreviation: [0.3233] ἔζη
  Abbreviation: [0.8787] ὄν
  Sent Starter: [97.8234] 'ἐπειδὴ'
  Sent Starter: [113.3762] 'οἱ'
  Sent Starter: [65.2843] 'εἰ'
  Sent Starter: [32.1611] 'τοιγαροῦν'
  Sent Starter: [36.0471] 'ἀλλὰ'
  Sent Starter: [186.0545] 'μετὰ'
  Sent Starter: [45.6612] 'ταύτην'
  Sent Starter: [335.0765] 'ἐνταῦθα'
  Sent Starter: [220.8901] 'καὶ'
  Sent Starter: [360.4958] 'ὁ'
  Sent Starter: [646.4387] 'ἐπεὶ'
  Sent Starter: [58.9281] 'ἀκούσας'
  Sent Starter: [53.6916] 'οὐκοῦν'
  Sent Starter: [58.7917] 'ταῦτα'
  Sent Starter: [124.8905] 'ἐκ'
  Sent Starter: [102.6241] 'ἔνθα'
  Sent Starter: [32.1611] 'καίτοι'
  Sent Starter: [47.4084] 'ἀκούσαντες'
  Sent Starter: [429.5321] 'ἐντεῦθεν'
```

LICENSE
-------
This software is, like the rest of the CLTK, licensed under the MIT license (see LICENSE). The texts included in `models/` come [from Perseus](http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0201) and are licensed under the [Creative Commons Attribution-ShareAlike 3.0 United States License](http://creativecommons.org/licenses/by-sa/3.0/us/).
