"""Generated message classes for transcoder version v1beta1.

This API converts video files into formats suitable for consumer distribution.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'transcoder'


class AdBreak(_messages.Message):
  r"""Ad break.

  Fields:
    startTimeOffset: Start time in seconds for the ad break, relative to the
      output file timeline. The default is `0s`.
  """

  startTimeOffset = _messages.StringField(1)


class Aes128Encryption(_messages.Message):
  r"""Configuration for AES-128 encryption.

  Fields:
    keyUri: Required. URI of the key delivery service. This URI is inserted
      into the M3U8 header.
  """

  keyUri = _messages.StringField(1)


class Animation(_messages.Message):
  r"""Animation types.

  Fields:
    animationEnd: End previous animation.
    animationFade: Display overlay object with fade animation.
    animationStatic: Display static overlay object.
  """

  animationEnd = _messages.MessageField('AnimationEnd', 1)
  animationFade = _messages.MessageField('AnimationFade', 2)
  animationStatic = _messages.MessageField('AnimationStatic', 3)


class AnimationEnd(_messages.Message):
  r"""End previous overlay animation from the video. Without AnimationEnd, the
  overlay object will keep the state of previous animation until the end of
  the video.

  Fields:
    startTimeOffset: The time to end overlay object, in seconds. Default: 0
  """

  startTimeOffset = _messages.StringField(1)


class AnimationFade(_messages.Message):
  r"""Display overlay object with fade animation.

  Enums:
    FadeTypeValueValuesEnum: Required. Type of fade animation: `FADE_IN` or
      `FADE_OUT`.

  Fields:
    endTimeOffset: The time to end the fade animation, in seconds. Default:
      `start_time_offset` + 1s
    fadeType: Required. Type of fade animation: `FADE_IN` or `FADE_OUT`.
    startTimeOffset: The time to start the fade animation, in seconds.
      Default: 0
    xy: Normalized coordinates based on output video resolution. Valid values:
      `0.0`\u2013`1.0`. `xy` is the upper-left coordinate of the overlay
      object.
  """

  class FadeTypeValueValuesEnum(_messages.Enum):
    r"""Required. Type of fade animation: `FADE_IN` or `FADE_OUT`.

    Values:
      FADE_TYPE_UNSPECIFIED: The fade type is not specified.
      FADE_IN: Fade the overlay object into view.
      FADE_OUT: Fade the overlay object out of view.
    """
    FADE_TYPE_UNSPECIFIED = 0
    FADE_IN = 1
    FADE_OUT = 2

  endTimeOffset = _messages.StringField(1)
  fadeType = _messages.EnumField('FadeTypeValueValuesEnum', 2)
  startTimeOffset = _messages.StringField(3)
  xy = _messages.MessageField('NormalizedCoordinate', 4)


class AnimationStatic(_messages.Message):
  r"""Display static overlay object.

  Fields:
    startTimeOffset: The time to start displaying the overlay object, in
      seconds. Default: 0
    xy: Normalized coordinates based on output video resolution. Valid values:
      `0.0`\u2013`1.0`. `xy` is the upper-left coordinate of the overlay
      object.
  """

  startTimeOffset = _messages.StringField(1)
  xy = _messages.MessageField('NormalizedCoordinate', 2)


class Audio(_messages.Message):
  r"""Audio preprocessing configuration.

  Fields:
    highBoost: Enable boosting high frequency components. The default is
      `false`.
    lowBoost: Enable boosting low frequency components. The default is
      `false`.
    lufs: Specify audio loudness normalization in loudness units relative to
      full scale (LUFS). Enter a value between -24 and 0, where -24 is the
      Advanced Television Systems Committee (ATSC A/85), -23 is the EU R128
      broadcast standard, -19 is the prior standard for online mono audio, -18
      is the ReplayGain standard, -16 is the prior standard for stereo audio,
      -14 is the new online audio standard recommended by Spotify, as well as
      Amazon Echo, and 0 disables normalization. The default is 0.
  """

  highBoost = _messages.BooleanField(1)
  lowBoost = _messages.BooleanField(2)
  lufs = _messages.FloatField(3)


class AudioAtom(_messages.Message):
  r"""The mapping for the `Job.edit_list` atoms with audio `EditAtom.inputs`.

  Fields:
    channels: List of `Channel`s for this audio stream. for in-depth
      explanation.
    key: Required. The `EditAtom.key` that references the atom with audio
      inputs in the `Job.edit_list`.
  """

  channels = _messages.MessageField('AudioChannel', 1, repeated=True)
  key = _messages.StringField(2)


class AudioChannel(_messages.Message):
  r"""The audio channel.

  Fields:
    inputs: List of `Job.inputs` for this audio channel.
  """

  inputs = _messages.MessageField('AudioChannelInput', 1, repeated=True)


class AudioChannelInput(_messages.Message):
  r"""Identifies which input file, track, and channel should be used.

  Fields:
    channel: Required. The zero-based index of the channel in the input file.
    gainDb: Audio volume control in dB. Negative values decrease volume,
      positive values increase. The default is 0.
    key: Required. The `Input.key` that identifies the input file.
    track: Required. The zero-based index of the track in the input file.
  """

  channel = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  gainDb = _messages.FloatField(2)
  key = _messages.StringField(3)
  track = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class AudioStream(_messages.Message):
  r"""Audio stream resource.

  Fields:
    bitrateBps: Required. Audio bitrate in bits per second. Must be between 1
      and 10,000,000.
    channelCount: Number of audio channels. Must be between 1 and 6. The
      default is 2.
    channelLayout: A list of channel names specifying layout of the audio
      channels. This only affects the metadata embedded in the container
      headers, if supported by the specified format. The default is `["fl",
      "fr"]`. Supported channel names: - 'fl' - Front left channel - 'fr' -
      Front right channel - 'sl' - Side left channel - 'sr' - Side right
      channel - 'fc' - Front center channel - 'lfe' - Low frequency
    codec: The codec for this audio stream. The default is `"aac"`. Supported
      audio codecs: - 'aac' - 'aac-he' - 'aac-he-v2' - 'mp3' - 'ac3' - 'eac3'
    mapping: The mapping for the `Job.edit_list` atoms with audio
      `EditAtom.inputs`.
    sampleRateHertz: The audio sample rate in Hertz. The default is 48000
      Hertz.
  """

  bitrateBps = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  channelCount = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  channelLayout = _messages.StringField(3, repeated=True)
  codec = _messages.StringField(4)
  mapping = _messages.MessageField('AudioAtom', 5, repeated=True)
  sampleRateHertz = _messages.IntegerField(6, variant=_messages.Variant.INT32)


class Color(_messages.Message):
  r"""Color preprocessing configuration.

  Fields:
    brightness: Control brightness of the video. Enter a value between -1 and
      1, where -1 is minimum brightness and 1 is maximum brightness. 0 is no
      change. The default is 0.
    contrast: Control black and white contrast of the video. Enter a value
      between -1 and 1, where -1 is minimum contrast and 1 is maximum
      contrast. 0 is no change. The default is 0.
    saturation: Control color saturation of the video. Enter a value between
      -1 and 1, where -1 is fully desaturated and 1 is maximum saturation. 0
      is no change. The default is 0.
  """

  brightness = _messages.FloatField(1)
  contrast = _messages.FloatField(2)
  saturation = _messages.FloatField(3)


class Deblock(_messages.Message):
  r"""Deblock preprocessing configuration.

  Fields:
    enabled: Enable deblocker. The default is `false`.
    strength: Set strength of the deblocker. Enter a value between 0 and 1.
      The higher the value, the stronger the block removal. 0 is no
      deblocking. The default is 0.
  """

  enabled = _messages.BooleanField(1)
  strength = _messages.FloatField(2)


class Denoise(_messages.Message):
  r"""Denoise preprocessing configuration.

  Fields:
    strength: Set strength of the denoise. Enter a value between 0 and 1. The
      higher the value, the smoother the image. 0 is no denoising. The default
      is 0.
    tune: Set the denoiser mode. The default is `"standard"`. Supported
      denoiser modes: - 'standard' - 'grain'
  """

  strength = _messages.FloatField(1)
  tune = _messages.StringField(2)


class EditAtom(_messages.Message):
  r"""Edit atom.

  Fields:
    endTimeOffset: End time in seconds for the atom, relative to the input
      file timeline. When `end_time_offset` is not specified, the `inputs` are
      used until the end of the atom.
    inputs: List of `Input.key`s identifying files that should be used in this
      atom. The listed `inputs` must have the same timeline.
    key: A unique key for this atom. Must be specified when using advanced
      mapping.
    startTimeOffset: Start time in seconds for the atom, relative to the input
      file timeline. The default is `0s`.
  """

  endTimeOffset = _messages.StringField(1)
  inputs = _messages.StringField(2, repeated=True)
  key = _messages.StringField(3)
  startTimeOffset = _messages.StringField(4)


class ElementaryStream(_messages.Message):
  r"""Encoding of an input file such as an audio, video, or text track.
  Elementary streams must be packaged before mapping and sharing between
  different output formats.

  Fields:
    audioStream: Encoding of an audio stream.
    key: A unique key for this elementary stream.
    textStream: Encoding of a text stream. For example, closed captions or
      subtitles.
    videoStream: Encoding of a video stream.
  """

  audioStream = _messages.MessageField('AudioStream', 1)
  key = _messages.StringField(2)
  textStream = _messages.MessageField('TextStream', 3)
  videoStream = _messages.MessageField('VideoStream', 4)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } The JSON
  representation for `Empty` is empty JSON object `{}`.
  """



class Encryption(_messages.Message):
  r"""Encryption settings.

  Fields:
    aes128: Configuration for AES-128 encryption.
    iv: Required. 128 bit Initialization Vector (IV) represented as lowercase
      hexadecimal digits.
    key: Required. 128 bit encryption key represented as lowercase hexadecimal
      digits.
    mpegCenc: Configuration for MPEG Common Encryption (MPEG-CENC).
    sampleAes: Configuration for SAMPLE-AES encryption.
  """

  aes128 = _messages.MessageField('Aes128Encryption', 1)
  iv = _messages.StringField(2)
  key = _messages.StringField(3)
  mpegCenc = _messages.MessageField('MpegCommonEncryption', 4)
  sampleAes = _messages.MessageField('SampleAesEncryption', 5)


class FailureDetail(_messages.Message):
  r"""Additional information about the reasons for the failure.

  Fields:
    description: A description of the failure.
  """

  description = _messages.StringField(1)


class Image(_messages.Message):
  r"""Overlaid jpeg image.

  Fields:
    alpha: Target image opacity. Valid values: `1` (solid, default), `0`
      (transparent).
    resolution: Normalized image resolution, based on output video resolution.
      Valid values: `0.0`\u2013`1.0`. To respect the original image aspect
      ratio, set either `x` or `y` to `0.0`. To use the original image
      resolution, set both `x` and `y` to `0.0`.
    uri: Required. URI of the image in Cloud Storage. For example,
      `gs://bucket/inputs/image.jpeg`.
  """

  alpha = _messages.FloatField(1)
  resolution = _messages.MessageField('NormalizedCoordinate', 2)
  uri = _messages.StringField(3)


class Input(_messages.Message):
  r"""Input asset.

  Fields:
    key: A unique key for this input. Must be specified when using advanced
      mapping and edit lists.
    preprocessingConfig: Preprocessing configurations.
    uri: URI of the media. It must be stored in Cloud Storage. Example
      `gs://bucket/inputs/file.mp4`. If empty the value will be populated from
      `Job.input_uri`.
  """

  key = _messages.StringField(1)
  preprocessingConfig = _messages.MessageField('PreprocessingConfig', 2)
  uri = _messages.StringField(3)


class Job(_messages.Message):
  r"""Transcoding job resource.

  Enums:
    StateValueValuesEnum: Output only. The current state of the job.

  Fields:
    config: The configuration for this job.
    createTime: Output only. The time the job was created.
    endTime: Output only. The time the transcoding finished.
    failureDetails: Output only. List of failure details. This property may
      contain additional information about the failure when `failure_reason`
      is present.
    failureReason: Output only. A description of the reason for the failure.
      This property is always present when `state` is `FAILED`.
    inputUri: Input only. Specify the `input_uri` to populate empty `uri`
      fields in each element of `Job.config.inputs` or
      `JobTemplate.config.inputs` when using template. URI of the media. It
      must be stored in Cloud Storage. For example,
      `gs://bucket/inputs/file.mp4`.
    name: The resource name of the job. Format:
      `projects/{project}/locations/{location}/jobs/{job}`
    originUri: Output only. The origin URI.
    outputUri: Input only. Specify the `output_uri` to populate an empty
      `Job.config.output.uri` or `JobTemplate.config.output.uri` when using
      template. URI for the output file(s). For example, `gs://my-
      bucket/outputs/`.
    priority: Specify the priority of the job. Enter a value between 0 and
      100, where 0 is the lowest priority and 100 is the highest priority. The
      default is 0.
    progress: Output only. Estimated fractional progress, from `0` to `1` for
      each step.
    startTime: Output only. The time the transcoding started.
    state: Output only. The current state of the job.
    templateId: Input only. Specify the `template_id` to use for populating
      `Job.config`. The default is `preset/web-hd`. Preset Transcoder
      templates: - `preset/{preset_id}` - User defined JobTemplate:
      `{job_template_id}`
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The current state of the job.

    Values:
      PROCESSING_STATE_UNSPECIFIED: The processing state is not specified.
      PENDING: The job is enqueued and will be picked up for processing soon.
      RUNNING: The job is being processed.
      SUCCEEDED: The job has been completed successfully.
      FAILED: The job has failed. For additional information, see
        `failure_reason` and `failure_details`
    """
    PROCESSING_STATE_UNSPECIFIED = 0
    PENDING = 1
    RUNNING = 2
    SUCCEEDED = 3
    FAILED = 4

  config = _messages.MessageField('JobConfig', 1)
  createTime = _messages.StringField(2)
  endTime = _messages.StringField(3)
  failureDetails = _messages.MessageField('FailureDetail', 4, repeated=True)
  failureReason = _messages.StringField(5)
  inputUri = _messages.StringField(6)
  name = _messages.StringField(7)
  originUri = _messages.MessageField('OriginUri', 8)
  outputUri = _messages.StringField(9)
  priority = _messages.IntegerField(10, variant=_messages.Variant.INT32)
  progress = _messages.MessageField('Progress', 11)
  startTime = _messages.StringField(12)
  state = _messages.EnumField('StateValueValuesEnum', 13)
  templateId = _messages.StringField(14)


class JobConfig(_messages.Message):
  r"""Job configuration

  Fields:
    adBreaks: List of ad breaks. Specifies where to insert ad break tags in
      the output manifests.
    editList: List of `Edit atom`s. Defines the ultimate timeline of the
      resulting file or manifest.
    elementaryStreams: List of elementary streams.
    inputs: List of input assets stored in Cloud Storage.
    manifests: List of output manifests.
    muxStreams: List of multiplexing settings for output streams.
    output: Output configuration.
    overlays: List of overlays on the output video, in descending Z-order.
    pubsubDestination: Destination on Pub/Sub.
    spriteSheets: List of output sprite sheets.
  """

  adBreaks = _messages.MessageField('AdBreak', 1, repeated=True)
  editList = _messages.MessageField('EditAtom', 2, repeated=True)
  elementaryStreams = _messages.MessageField('ElementaryStream', 3, repeated=True)
  inputs = _messages.MessageField('Input', 4, repeated=True)
  manifests = _messages.MessageField('Manifest', 5, repeated=True)
  muxStreams = _messages.MessageField('MuxStream', 6, repeated=True)
  output = _messages.MessageField('Output', 7)
  overlays = _messages.MessageField('Overlay', 8, repeated=True)
  pubsubDestination = _messages.MessageField('PubsubDestination', 9)
  spriteSheets = _messages.MessageField('SpriteSheet', 10, repeated=True)


class JobTemplate(_messages.Message):
  r"""Transcoding job template resource.

  Fields:
    config: The configuration for this template.
    name: The resource name of the job template. Format:
      `projects/{project}/locations/{location}/jobTemplates/{job_template}`
  """

  config = _messages.MessageField('JobConfig', 1)
  name = _messages.StringField(2)


class ListJobTemplatesResponse(_messages.Message):
  r"""Response message for `TranscoderService.ListJobTemplates`.

  Fields:
    jobTemplates: List of job templates in the specified region.
    nextPageToken: The pagination token.
  """

  jobTemplates = _messages.MessageField('JobTemplate', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListJobsResponse(_messages.Message):
  r"""Response message for `TranscoderService.ListJobs`.

  Fields:
    jobs: List of jobs in the specified region.
    nextPageToken: The pagination token.
  """

  jobs = _messages.MessageField('Job', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class Manifest(_messages.Message):
  r"""Manifest configuration.

  Enums:
    TypeValueValuesEnum: Required. Type of the manifest, can be "HLS" or
      "DASH".

  Fields:
    fileName: The name of the generated file. The default is `"master"` with
      the extension suffix corresponding to the `Manifest.type`.
    muxStreams: Required. List of user given `MuxStream.key`s that should
      appear in this manifest. When `Manifest.type` is `HLS`, a media manifest
      with name `MuxStream.key` and `.m3u8` extension is generated for each
      element of the `Manifest.mux_streams`.
    type: Required. Type of the manifest, can be "HLS" or "DASH".
  """

  class TypeValueValuesEnum(_messages.Enum):
    r"""Required. Type of the manifest, can be "HLS" or "DASH".

    Values:
      MANIFEST_TYPE_UNSPECIFIED: The manifest type is not specified.
      HLS: Create `"HLS"` manifest. The corresponding file extension is
        `".m3u8"`.
      DASH: Create `"DASH"` manifest. The corresponding file extension is
        `".mpd"`.
    """
    MANIFEST_TYPE_UNSPECIFIED = 0
    HLS = 1
    DASH = 2

  fileName = _messages.StringField(1)
  muxStreams = _messages.StringField(2, repeated=True)
  type = _messages.EnumField('TypeValueValuesEnum', 3)


class MpegCommonEncryption(_messages.Message):
  r"""Configuration for MPEG Common Encryption (MPEG-CENC).

  Fields:
    keyId: Required. 128 bit Key ID represented as lowercase hexadecimal
      digits for use with common encryption.
    scheme: Required. Specify the encryption scheme. Supported encryption
      schemes: - 'cenc' - 'cbcs'
  """

  keyId = _messages.StringField(1)
  scheme = _messages.StringField(2)


class MuxStream(_messages.Message):
  r"""Multiplexing settings for output stream.

  Fields:
    container: The container format. The default is `"mp4"` Supported
      container formats: - 'ts' - 'fmp4'- the corresponding file extension is
      `".m4s"` - 'mp4' - 'vtt'
    elementaryStreams: List of `ElementaryStream.key`s multiplexed in this
      stream.
    encryption: Encryption settings.
    fileName: The name of the generated file. The default is `MuxStream.key`
      with the extension suffix corresponding to the `MuxStream.container`.
      Individual segments also have an incremental 10-digit zero-padded suffix
      starting from 0 before the extension, such as
      `"mux_stream0000000123.ts"`.
    key: A unique key for this multiplexed stream. HLS media manifests will be
      named `MuxStream.key` with the `".m3u8"` extension suffix.
    segmentSettings: Segment settings for `"ts"`, `"fmp4"` and `"vtt"`.
  """

  container = _messages.StringField(1)
  elementaryStreams = _messages.StringField(2, repeated=True)
  encryption = _messages.MessageField('Encryption', 3)
  fileName = _messages.StringField(4)
  key = _messages.StringField(5)
  segmentSettings = _messages.MessageField('SegmentSettings', 6)


class NormalizedCoordinate(_messages.Message):
  r"""2D normalized coordinates. Default: `{0.0, 0.0}`

  Fields:
    x: Normalized x coordinate.
    y: Normalized y coordinate.
  """

  x = _messages.FloatField(1)
  y = _messages.FloatField(2)


class OriginUri(_messages.Message):
  r"""The origin URI.

  Fields:
    dash: Dash manifest URI. If multiple Dash manifests are created, only the
      first one is listed.
    hls: HLS master manifest URI. If multiple HLS master manifests are created
      only first one is listed.
  """

  dash = _messages.StringField(1)
  hls = _messages.StringField(2)


class Output(_messages.Message):
  r"""Location of output file(s) in a Cloud Storage bucket.

  Fields:
    uri: URI for the output file(s). For example, `gs://my-bucket/outputs/`.
      If empty the value is populated from `Job.output_uri`.
  """

  uri = _messages.StringField(1)


class Overlay(_messages.Message):
  r"""Overlay configuration.

  Fields:
    animations: List of Animations. The list should be chronological, without
      any time overlap.
    image: Image overlay.
  """

  animations = _messages.MessageField('Animation', 1, repeated=True)
  image = _messages.MessageField('Image', 2)


class PreprocessingConfig(_messages.Message):
  r"""Preprocessing configurations.

  Fields:
    audio: Audio preprocessing configuration.
    color: Color preprocessing configuration.
    deblock: Deblock preprocessing configuration.
    denoise: Denoise preprocessing configuration.
  """

  audio = _messages.MessageField('Audio', 1)
  color = _messages.MessageField('Color', 2)
  deblock = _messages.MessageField('Deblock', 3)
  denoise = _messages.MessageField('Denoise', 4)


class Progress(_messages.Message):
  r"""Estimated fractional progress for each step, from `0` to `1`.

  Fields:
    analyzed: Estimated fractional progress for `analyzing` step.
    encoded: Estimated fractional progress for `encoding` step.
    notified: Estimated fractional progress for `notifying` step.
    uploaded: Estimated fractional progress for `uploading` step.
  """

  analyzed = _messages.FloatField(1)
  encoded = _messages.FloatField(2)
  notified = _messages.FloatField(3)
  uploaded = _messages.FloatField(4)


class PubsubDestination(_messages.Message):
  r"""A Pub/Sub destination.

  Fields:
    topic: The name of the Pub/Sub topic to publish job completion
      notification to. For example: `projects/{project}/topics/{topic}`.
  """

  topic = _messages.StringField(1)


class SampleAesEncryption(_messages.Message):
  r"""Configuration for SAMPLE-AES encryption.

  Fields:
    keyUri: Required. URI of the key delivery service. This URI is inserted
      into the M3U8 header.
  """

  keyUri = _messages.StringField(1)


class SegmentSettings(_messages.Message):
  r"""Segment settings for `"ts"`, `"fmp4"` and `"vtt"`.

  Fields:
    individualSegments: Required. Create an individual segment file. The
      default is `false`.
    segmentDuration: Duration of the segments in seconds. The default is
      `"6.0s"`.
  """

  individualSegments = _messages.BooleanField(1)
  segmentDuration = _messages.StringField(2)


class SpriteSheet(_messages.Message):
  r"""Sprite sheet configuration.

  Fields:
    columnCount: The maximum number of sprites per row in a sprite sheet. The
      default is 0, which indicates no maximum limit.
    endTimeOffset: End time in seconds, relative to the output file timeline.
      When `end_time_offset` is not specified, the sprites are generated until
      the end of the output file.
    filePrefix: Required. File name prefix for the generated sprite sheets.
      Each sprite sheet has an incremental 10-digit zero-padded suffix
      starting from 0 before the extension, such as
      `"sprite_sheet0000000123.jpeg"`.
    format: Format type. The default is `"jpeg"`. Supported formats: - 'jpeg'
    interval: Starting from `0s`, create sprites at regular intervals. Specify
      the interval value in seconds.
    rowCount: The maximum number of rows per sprite sheet. When the sprite
      sheet is full, a new sprite sheet is created. The default is 0, which
      indicates no maximum limit.
    spriteHeightPixels: Required. The height of sprite in pixels. Must be an
      even integer.
    spriteWidthPixels: Required. The width of sprite in pixels. Must be an
      even integer.
    startTimeOffset: Start time in seconds, relative to the output file
      timeline. Determines the first sprite to pick. The default is `0s`.
    totalCount: Total number of sprites. Create the specified number of
      sprites distributed evenly across the timeline of the output media. The
      default is 100.
  """

  columnCount = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  endTimeOffset = _messages.StringField(2)
  filePrefix = _messages.StringField(3)
  format = _messages.StringField(4)
  interval = _messages.StringField(5)
  rowCount = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  spriteHeightPixels = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  spriteWidthPixels = _messages.IntegerField(8, variant=_messages.Variant.INT32)
  startTimeOffset = _messages.StringField(9)
  totalCount = _messages.IntegerField(10, variant=_messages.Variant.INT32)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class TextAtom(_messages.Message):
  r"""The mapping for the `Job.edit_list` atoms with text `EditAtom.inputs`.

  Fields:
    inputs: List of `Job.inputs` that should be embedded in this atom. Only
      one input is supported.
    key: Required. The `EditAtom.key` that references atom with text inputs in
      the `Job.edit_list`.
  """

  inputs = _messages.MessageField('TextInput', 1, repeated=True)
  key = _messages.StringField(2)


class TextInput(_messages.Message):
  r"""Identifies which input file and track should be used.

  Fields:
    key: Required. The `Input.key` that identifies the input file.
    track: Required. The zero-based index of the track in the input file.
  """

  key = _messages.StringField(1)
  track = _messages.IntegerField(2, variant=_messages.Variant.INT32)


class TextStream(_messages.Message):
  r"""Encoding of a text stream. For example, closed captions or subtitles.

  Fields:
    codec: The codec for this text stream. The default is `"webvtt"`.
      Supported text codecs: - 'srt' - 'ttml' - 'cea608' - 'cea708' - 'webvtt'
    languageCode: Required. The BCP-47 language code, such as `"en-US"` or
      `"sr-Latn"`. For more information, see
      https://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    mapping: The mapping for the `Job.edit_list` atoms with text
      `EditAtom.inputs`.
  """

  codec = _messages.StringField(1)
  languageCode = _messages.StringField(2)
  mapping = _messages.MessageField('TextAtom', 3, repeated=True)


class TranscoderProjectsLocationsJobTemplatesCreateRequest(_messages.Message):
  r"""A TranscoderProjectsLocationsJobTemplatesCreateRequest object.

  Fields:
    jobTemplate: A JobTemplate resource to be passed as the request body.
    jobTemplateId: Required. The ID to use for the job template, which will
      become the final component of the job template's resource name. This
      value should be 4-63 characters, and valid characters must match the
      regular expression `a-zA-Z*`.
    parent: Required. The parent location to create this job template. Format:
      `projects/{project}/locations/{location}`
  """

  jobTemplate = _messages.MessageField('JobTemplate', 1)
  jobTemplateId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class TranscoderProjectsLocationsJobTemplatesDeleteRequest(_messages.Message):
  r"""A TranscoderProjectsLocationsJobTemplatesDeleteRequest object.

  Fields:
    name: Required. The name of the job template to delete.
      `projects/{project}/locations/{location}/jobTemplates/{job_template}`
  """

  name = _messages.StringField(1, required=True)


class TranscoderProjectsLocationsJobTemplatesGetRequest(_messages.Message):
  r"""A TranscoderProjectsLocationsJobTemplatesGetRequest object.

  Fields:
    name: Required. The name of the job template to retrieve. Format:
      `projects/{project}/locations/{location}/jobTemplates/{job_template}`
  """

  name = _messages.StringField(1, required=True)


class TranscoderProjectsLocationsJobTemplatesListRequest(_messages.Message):
  r"""A TranscoderProjectsLocationsJobTemplatesListRequest object.

  Fields:
    pageSize: The maximum number of items to return.
    pageToken: The `next_page_token` value returned from a previous List
      request, if any.
    parent: Required. The parent location from which to retrieve the
      collection of job templates. Format:
      `projects/{project}/locations/{location}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class TranscoderProjectsLocationsJobsCreateRequest(_messages.Message):
  r"""A TranscoderProjectsLocationsJobsCreateRequest object.

  Fields:
    job: A Job resource to be passed as the request body.
    parent: Required. The parent location to create and process this job.
      Format: `projects/{project}/locations/{location}`
  """

  job = _messages.MessageField('Job', 1)
  parent = _messages.StringField(2, required=True)


class TranscoderProjectsLocationsJobsDeleteRequest(_messages.Message):
  r"""A TranscoderProjectsLocationsJobsDeleteRequest object.

  Fields:
    name: Required. The name of the job to delete. Format:
      `projects/{project}/locations/{location}/jobs/{job}`
  """

  name = _messages.StringField(1, required=True)


class TranscoderProjectsLocationsJobsGetRequest(_messages.Message):
  r"""A TranscoderProjectsLocationsJobsGetRequest object.

  Fields:
    name: Required. The name of the job to retrieve. Format:
      `projects/{project}/locations/{location}/jobs/{job}`
  """

  name = _messages.StringField(1, required=True)


class TranscoderProjectsLocationsJobsListRequest(_messages.Message):
  r"""A TranscoderProjectsLocationsJobsListRequest object.

  Fields:
    pageSize: The maximum number of items to return.
    pageToken: The `next_page_token` value returned from a previous List
      request, if any.
    parent: Required. Format: `projects/{project}/locations/{location}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class VideoStream(_messages.Message):
  r"""Video stream resource.

  Fields:
    allowOpenGop: Specifies whether an open Group of Pictures (GOP) structure
      should be allowed or not. The default is `false`.
    aqStrength: Specify the intensity of the adaptive quantizer (AQ). Must be
      between 0 and 1, where 0 disables the quantizer and 1 maximizes the
      quantizer. A higher value equals a lower bitrate but smoother image. The
      default is 0.
    bFrameCount: The number of consecutive B-frames. Must be greater than or
      equal to zero. Must be less than `VideoStream.gop_frame_count` if set.
      The default is 0.
    bPyramid: Allow B-pyramid for reference frame selection. This may not be
      supported on all decoders. The default is `false`.
    bitrateBps: Required. The video bitrate in bits per second. Must be
      between 1 and 1,000,000,000.
    codec: Codec type. The default is `"h264"`. Supported codecs: - 'h264' -
      'h265' - 'vp9'
    crfLevel: Target CRF level. Must be between 10 and 36, where 10 is the
      highest quality and 36 is the most efficient compression. The default is
      21.
    enableTwoPass: Use two-pass encoding strategy to achieve better video
      quality. `VideoStream.rate_control_mode` must be `"vbr"`. The default is
      `false`.
    entropyCoder: The entropy coder to use. The default is `"cabac"`.
      Supported entropy coders: - 'cavlc' - 'cabac'
    frameRate: Required. The target video frame rate in frames per second
      (FPS). Must be less than or equal to 120. Will default to the input
      frame rate if larger than the input frame rate. The API will generate an
      output FPS that is divisible by the input FPS, and smaller or equal to
      the target FPS. The following table shows the computed video FPS given
      the target FPS (in parenthesis) and input FPS (in the first column): | |
      (30) | (60) | (25) | (50) | |--------|--------|--------|------|------| |
      240 | Fail | Fail | Fail | Fail | | 120 | 30 | 60 | 20 | 30 | | 100 | 25
      | 50 | 20 | 30 | | 50 | 25 | 50 | 20 | 30 | | 60 | 30 | 60 | 20 | 30 | |
      59.94 | 29.97 | 59.94 | 20 | 30 | | 48 | 24 | 48 | 20 | 30 | | 30 | 30 |
      30 | 20 | 30 | | 25 | 25 | 25 | 20 | 30 | | 24 | 24 | 24 | 20 | 30 | |
      23.976 | 23.976 | 23.976 | 20 | 30 | | 15 | 15 | 15 | 20 | 30 | | 12 |
      12 | 12 | 20 | 30 | | 10 | 10 | 10 | 20 | 30 |
    gopDuration: Select the GOP size based on the specified duration. The
      default is `"3s"`.
    gopFrameCount: Select the GOP size based on the specified frame count.
      Must be greater than zero.
    heightPixels: The height of the video in pixels. Must be an even integer.
      When not specified, the height is adjusted to match the specified width
      and input aspect ratio. If both are omitted, the input height is used.
    pixelFormat: Pixel format to use. The default is `"yuv420p"`. Supported
      pixel formats: - 'yuv420p' pixel format. - 'yuv422p' pixel format. -
      'yuv444p' pixel format. - 'yuv420p10' 10-bit HDR pixel format. -
      'yuv422p10' 10-bit HDR pixel format. - 'yuv444p10' 10-bit HDR pixel
      format. - 'yuv420p12' 12-bit HDR pixel format. - 'yuv422p12' 12-bit HDR
      pixel format. - 'yuv444p12' 12-bit HDR pixel format.
    preset: Enforce specified codec preset. The default is `"veryfast"`.
    profile: Enforce specified codec profile. The default is `"high"`.
      Supported codec profiles: - 'baseline' - 'main' - 'high'
    rateControlMode: Specify the `rate_control_mode`. The default is `"vbr"`.
      Supported rate control modes: - 'vbr' - variable bitrate - 'crf' -
      constant rate factor
    tune: Enforce specified codec tune.
    vbvFullnessBits: Initial fullness of the Video Buffering Verifier (VBV)
      buffer in bits. Must be greater than zero. The default is equal to 90%
      of `VideoStream.vbv_size_bits`.
    vbvSizeBits: Size of the Video Buffering Verifier (VBV) buffer in bits.
      Must be greater than zero. The default is equal to
      `VideoStream.bitrate_bps`.
    widthPixels: The width of the video in pixels. Must be an even integer.
      When not specified, the width is adjusted to match the specified height
      and input aspect ratio. If both are omitted, the input width is used.
  """

  allowOpenGop = _messages.BooleanField(1)
  aqStrength = _messages.FloatField(2)
  bFrameCount = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  bPyramid = _messages.BooleanField(4)
  bitrateBps = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  codec = _messages.StringField(6)
  crfLevel = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  enableTwoPass = _messages.BooleanField(8)
  entropyCoder = _messages.StringField(9)
  frameRate = _messages.FloatField(10)
  gopDuration = _messages.StringField(11)
  gopFrameCount = _messages.IntegerField(12, variant=_messages.Variant.INT32)
  heightPixels = _messages.IntegerField(13, variant=_messages.Variant.INT32)
  pixelFormat = _messages.StringField(14)
  preset = _messages.StringField(15)
  profile = _messages.StringField(16)
  rateControlMode = _messages.StringField(17)
  tune = _messages.StringField(18)
  vbvFullnessBits = _messages.IntegerField(19, variant=_messages.Variant.INT32)
  vbvSizeBits = _messages.IntegerField(20, variant=_messages.Variant.INT32)
  widthPixels = _messages.IntegerField(21, variant=_messages.Variant.INT32)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
