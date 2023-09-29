WORDING =\
{
	'python_not_supported': 'Python version is not supported, upgrade to {version} or higher',
	'ffmpeg_not_installed': 'FFMpeg is not installed',
	'onnxruntime_help': 'select the onnxruntime to be installed',
	'source_help': 'select a source image',
	'target_help': 'select a target image or video',
	'output_help': 'specify the output file or directory',
	'frame_processors_help': 'choose from the available frame processors (choices: {choices}, ...)',
	'models_help': 'choose from the available models',
	'ui_layouts_help': 'choose from the available ui layouts (choices: {choices}, ...)',
	'keep_fps_help': 'preserve the frames per second (fps) of the target',
	'keep_temp_help': 'retain temporary frames after processing',
	'skip_audio_help': 'omit audio from the target',
	'face_recognition_help': 'specify the method for face recognition',
	'face_analyser_direction_help': 'specify the direction used for face analysis',
	'face_analyser_age_help': 'specify the age used for face analysis',
	'face_analyser_gender_help': 'specify the gender used for face analysis',
	'reference_face_position_help': 'specify the position of the reference face',
	'reference_face_distance_help': 'specify the distance between the reference face and the target face',
	'reference_frame_number_help': 'specify the number of the reference frame',
	'trim_frame_start_help': 'specify the start frame for extraction',
	'trim_frame_end_help': 'specify the end frame for extraction',
	'temp_frame_format_help': 'specify the image format used for frame extraction',
	'temp_frame_quality_help': 'specify the image quality used for frame extraction',
	'output_image_quality_help': 'specify the quality used for the output image',
	'output_video_encoder_help': 'specify the encoder used for the output video',
	'output_video_quality_help': 'specify the quality used for the output video',
	'max_memory_help': 'specify the maximum amount of ram to be used (in gb)',
	'execution_providers_help': 'choose from the available execution providers (choices: {choices}, ...)',
	'execution_thread_count_help': 'specify the number of execution threads',
	'execution_queue_count_help': 'specify the number of execution queries',
	'skip_download_help': 'omit automate downloads and lookups',
	'headless_help': 'run the program in headless mode',
	'creating_temp': 'Creating temporary resources',
	'extracting_frames_fps': 'Extracting frames with {fps} FPS',
	'processing': 'Processing',
	'downloading': 'Downloading',
	'temp_frames_not_found': 'Temporary frames not found',
	'compressing_image': 'Compressing image',
	'compressing_image_failed': 'Compressing image failed',
	'merging_video_fps': 'Merging video with {fps} FPS',
	'merging_video_failed': 'Merging video failed',
	'skipping_audio': 'Skipping audio',
	'restoring_audio': 'Restoring audio',
	'restoring_audio_failed': 'Restoring audio failed',
	'clearing_temp': 'Clearing temporary resources',
	'processing_image_succeed': 'Processing to image succeed',
	'processing_image_failed': 'Processing to image failed',
	'processing_video_succeed': 'Processing to video succeed',
	'processing_video_failed': 'Processing to video failed',
	'model_download_not_done': 'Download of the model is not done',
	'model_file_not_present': 'File of the model is not present',
	'select_image_source': 'Select an image for source path',
	'select_image_or_video_target': 'Select an image or video for target path',
	'select_file_or_directory_output': 'Select an file or directory for output path',
	'no_source_face_detected': 'No source face detected',
	'frame_processor_not_loaded': 'Frame processor {frame_processor} could not be loaded',
	'frame_processor_not_implemented': 'Frame processor {frame_processor} not implemented correctly',
	'ui_layout_not_loaded': 'UI layout {ui_layout} could not be loaded',
	'ui_layout_not_implemented': 'UI layout {ui_layout} not implemented correctly',
	'start_button_label': 'START',
	'stop_button_label': 'STOP',
	'clear_button_label': 'CLEAR',
	'benchmark_runs_checkbox_group_label': 'BENCHMARK RUNS',
	'benchmark_results_dataframe_label': 'BENCHMARK RESULTS',
	'benchmark_cycles_slider_label': 'BENCHMARK CYCLES',
	'execution_providers_checkbox_group_label': 'EXECUTION PROVIDERS',
	'execution_thread_count_slider_label': 'EXECUTION THREAD COUNT',
	'execution_queue_count_slider_label': 'EXECUTION QUEUE COUNT',
	'face_analyser_direction_dropdown_label': 'FACE ANALYSER DIRECTION',
	'face_analyser_age_dropdown_label': 'FACE ANALYSER AGE',
	'face_analyser_gender_dropdown_label': 'FACE ANALYSER GENDER',
	'reference_face_gallery_label': 'REFERENCE FACE',
	'face_recognition_dropdown_label': 'FACE RECOGNITION',
	'reference_face_distance_slider_label': 'REFERENCE FACE DISTANCE',
	'max_memory_slider_label': 'MAX MEMORY',
	'output_image_or_video_label': 'OUTPUT',
	'output_path_textbox_label': 'OUTPUT PATH',
	'output_image_quality_slider_label': 'OUTPUT IMAGE QUALITY',
	'output_video_encoder_dropdown_label': 'OUTPUT VIDEO ENCODER',
	'output_video_quality_slider_label': 'OUTPUT VIDEO QUALITY',
	'preview_image_label': 'PREVIEW',
	'preview_frame_slider_label': 'PREVIEW FRAME',
	'frame_processors_checkbox_group_label': 'FRAME PROCESSORS',
	'face_swapper_model_dropdown_label': 'FACE SWAPPER MODEL',
	'face_enhancer_model_dropdown_label': 'FACE ENHANCER MODEL',
	'frame_enhancer_model_dropdown_label': 'FRAME ENHANCER MODEL',
	'common_options_checkbox_group_label': 'SETTINGS',
	'temp_frame_format_dropdown_label': 'TEMP FRAME FORMAT',
	'temp_frame_quality_slider_label': 'TEMP FRAME QUALITY',
	'trim_frame_start_slider_label': 'TRIM FRAME START',
	'trim_frame_end_slider_label': 'TRIM FRAME END',
	'source_file_label': 'SOURCE',
	'target_file_label': 'TARGET',
	'webcam_image_label': 'WEBCAM',
	'webcam_mode_radio_label': 'WEBCAM MODE',
	'webcam_resolution_dropdown': 'WEBCAM RESOLUTION',
	'webcam_fps_slider': 'WEBCAM FPS',
	'point': '.',
	'comma': ',',
	'colon': ':',
	'question_mark': '?',
	'exclamation_mark': '!'
}


def get(key : str) -> str:
	return WORDING[key]
