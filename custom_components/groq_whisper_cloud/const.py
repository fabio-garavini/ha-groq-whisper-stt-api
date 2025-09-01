"""Constants for the GroqCloud Whisper integration."""

DOMAIN = "groqcloud_whisper"

CONF_PROMPT = "prompt"
CONF_TEMPERATURE = "temperature"

SUPPORTED_MODELS = [
    "distil-whisper-large-v3-en",
    "whisper-large-v3"
]

SUPPORTED_LANGUAGES = [
    "af",
    "ar",
    "hy",
    "az",
    "be",
    "bs",
    "bg",
    "ca",
    "zh",
    "hr",
    "cs",
    "da",
    "nl",
    "en",
    "et",
    "fi",
    "fr",
    "gl",
    "de",
    "el",
    "he",
    "hi",
    "hu",
    "is",
    "id",
    "it",
    "ja",
    "kn",
    "kk",
    "ko",
    "lv",
    "lt",
    "mk",
    "ms",
    "mr",
    "mi",
    "ne",
    "no",
    "fa",
    "pl",
    "pt",
    "ro",
    "ru",
    "sr",
    "sk",
    "sl",
    "es",
    "sw",
    "sv",
    "tl",
    "ta",
    "th",
    "tr",
    "uk",
    "ur",
    "vi",
    "cy"
]

DEFAULT_NAME = "GroqCloud Whisper"
DEFAULT_WHISPER_MODEL = SUPPORTED_MODELS[0]
DEFAULT_PROMPT = ""
DEFAULT_TEMPERATURE = 0