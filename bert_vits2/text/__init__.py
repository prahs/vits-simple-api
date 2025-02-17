from bert_vits2.text.symbols import *
from .chinese_bert import get_bert_feature as zh_bert
from .english_bert_mock import get_bert_feature as en_bert
from .japanese_bert import get_bert_feature as ja_bert


def cleaned_text_to_sequence(cleaned_text, tones, language, _symbol_to_id):
    """Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
    """
    phones = [_symbol_to_id[symbol] for symbol in cleaned_text]
    tone_start = language_tone_start_map[language]
    tones = [i + tone_start for i in tones]
    lang_id = language_id_map[language]
    lang_ids = [lang_id for i in phones]
    return phones, tones, lang_ids


def get_bert(norm_text, word2ph, language):
    lang_bert_func_map = {"zh": zh_bert, "en": en_bert, "ja": ja_bert}
    bert = lang_bert_func_map[language](norm_text, word2ph)
    return bert
