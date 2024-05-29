from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from app.core.settings import settings

class ModelLoader:
    _model = None
    _tokenizer = None
    _autocomplete_pipeline = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            model_name = settings.model_name
            cls._model = AutoModelForCausalLM.from_pretrained(model_name)
            cls._tokenizer = AutoTokenizer.from_pretrained(model_name)
            cls._autocomplete_pipeline = pipeline("text-generation", model=cls._model, tokenizer=cls._tokenizer)
        return cls._model, cls._tokenizer, cls._autocomplete_pipeline

model, tokenizer, autocomplete_pipeline = ModelLoader.get_model()