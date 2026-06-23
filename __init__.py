from .ltx_keyframer import LTXKeyframer
from .multi_image_loader import MultiImageLoader
from .ltx_sequencer import LTXSequencer
from .speech_length_calculator import SpeechLengthCalculator
from .load_audio_ui import LoadAudioUI
from .load_video_ui import LoadVideoUI
from .ltx_director import LTXDirector
from .ltx_director_guide import LTXDirectorGuide, LTXDirectorCropGuides
from .ltx_director_with_reference_image import LTXDirectorWithReferenceImage
from .ltx_director_with_more_output import LTXDirectorWithMoreOutput
from .ltx_director_with_grid_image import LTXDirectorWithGridImage
from .ltx_director_with_grid_image_v2 import LTXDirectorWithGridImageV2
from .latent_slice import CleanLatentSlice
from comfy_api.latest import ComfyExtension, io
from typing_extensions import override

class PromptRelay(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            LTXDirector,
            LTXDirectorWithReferenceImage,
            LTXDirectorWithMoreOutput,
            LTXDirectorWithGridImage,
            LTXDirectorWithGridImageV2,
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
    "LTXDirectorGuide": LTXDirectorGuide,
    "LTXDirectorCropGuides": LTXDirectorCropGuides,
    "LTXDirectorWithReferenceImage": LTXDirectorWithReferenceImage,
    "LTXDirectorWithMoreOutput": LTXDirectorWithMoreOutput,
    "LTXDirectorWithGridImage": LTXDirectorWithGridImage,
    "LTXDirectorWithGridImageV2": LTXDirectorWithGridImageV2,
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
    "LTXDirectorGuide": "LTX Director Guide",
    "LTXDirectorCropGuides": "LTX Director Crop Guides",
    "LTXDirectorWithReferenceImage": "LTX Director With Reference Image",
    "LTXDirectorWithMoreOutput": "LTX Director With More Output",
    "LTXDirectorWithGridImage": "LTX Director With Grid Image",
    "LTXDirectorWithGridImageV2": "LTX Director With Grid Image V2",
    "CleanLatentSlice": "Clean Latent Slice",
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
