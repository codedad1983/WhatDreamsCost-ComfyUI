from .ltx_keyframer import LTXKeyframer
from .multi_image_loader import MultiImageLoader
from .ltx_sequencer import LTXSequencer
from .speech_length_calculator import SpeechLengthCalculator
from .load_audio_ui import LoadAudioUI
from .load_video_ui import LoadVideoUI
from .ltx_director import LTXDirector
from .ltx_director_with_reference_image import LTXDirectorWithReferenceImage
from .ltx_director_guide import LTXDirectorGuide
from .latent_slice import CleanLatentSlice
from comfy_api.latest import ComfyExtension, io
from typing_extensions import override

class PromptRelay(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            LTXDirector,
            LTXDirectorWithReferenceImage,
            LTXDirectorGuide
        ]

async def comfy_entrypoint() -> PromptRelay:
    return PromptRelay()
    
NODE_CLASS_MAPPINGS = {
    "LTXKeyframer": LTXKeyframer,
    "MultiImageLoader": MultiImageLoader,
    "LTXSequencer": LTXSequencer,
    "SpeechLengthCalculator": SpeechLengthCalculator,
    "LoadAudioUI": LoadAudioUI,
    "LoadVideoUI": LoadVideoUI,
    "LTXDirector": LTXDirector,
    "LTXDirectorWithReferenceImage": LTXDirectorWithReferenceImage,
    "LTXDirectorGuide": LTXDirectorGuide,
    "CleanLatentSlice": CleanLatentSlice,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LTXKeyframer": "LTX Keyframer",
    "MultiImageLoader": "Multi Image Loader",
    "LTXSequencer": "LTX Sequencer",
    "SpeechLengthCalculator": "Speech Length Calculator",
    "LoadAudioUI": "Load Audio UI",
    "LoadVideoUI": "Load Video UI",
    "LTXDirector": "LTX Director",
    "LTXDirectorWithReferenceImage": "LTX Director With Reference Image",
    "LTXDirectorGuide": "LTX Director Guide",
    "CleanLatentSlice": "Clean Latent Slice",
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
