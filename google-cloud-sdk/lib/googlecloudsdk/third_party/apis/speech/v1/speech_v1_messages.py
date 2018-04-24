"""Generated message classes for speech version v1.

Converts audio to text by applying powerful neural network models.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'speech'


class LongRunningRecognizeRequest(_messages.Message):
  """The top-level message sent by the client for the `LongRunningRecognize`
  method.

  Fields:
    audio: *Required* The audio data to be recognized.
    config: *Required* Provides information to the recognizer that specifies
      how to process the request.
  """

  audio = _messages.MessageField('RecognitionAudio', 1)
  config = _messages.MessageField('RecognitionConfig', 2)


class Operation(_messages.Message):
  """This resource represents a long-running operation that is the result of a
  network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    """The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class RecognitionAudio(_messages.Message):
  """Contains audio data in the encoding specified in the `RecognitionConfig`.
  Either `content` or `uri` must be supplied. Supplying both or neither
  returns google.rpc.Code.INVALID_ARGUMENT. See [audio
  limits](https://cloud.google.com/speech/limits#content).

  Fields:
    content: The audio data bytes encoded as specified in `RecognitionConfig`.
      Note: as with all bytes fields, protobuffers use a pure binary
      representation, whereas JSON representations use base64.
    uri: URI that points to a file that contains audio data bytes as specified
      in `RecognitionConfig`. Currently, only Google Cloud Storage URIs are
      supported, which must be specified in the following format:
      `gs://bucket_name/object_name` (other URI formats return
      google.rpc.Code.INVALID_ARGUMENT). For more information, see [Request
      URIs](https://cloud.google.com/storage/docs/reference-uris).
  """

  content = _messages.BytesField(1)
  uri = _messages.StringField(2)


class RecognitionConfig(_messages.Message):
  """Provides information to the recognizer that specifies how to process the
  request.

  Enums:
    EncodingValueValuesEnum: Encoding of audio data sent in all
      `RecognitionAudio` messages. This field is optional for `FLAC` and `WAV`
      audio files and required for all other audio formats. For details, see
      AudioEncoding.

  Fields:
    enableWordTimeOffsets: *Optional* If `true`, the top result includes a
      list of words and the start and end time offsets (timestamps) for those
      words. If `false`, no word-level time offset information is returned.
      The default is `false`.
    encoding: Encoding of audio data sent in all `RecognitionAudio` messages.
      This field is optional for `FLAC` and `WAV` audio files and required for
      all other audio formats. For details, see AudioEncoding.
    languageCode: *Required* The language of the supplied audio as a
      [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag.
      Example: "en-US". See [Language
      Support](https://cloud.google.com/speech/docs/languages) for a list of
      the currently supported language codes.
    maxAlternatives: *Optional* Maximum number of recognition hypotheses to be
      returned. Specifically, the maximum number of
      `SpeechRecognitionAlternative` messages within each
      `SpeechRecognitionResult`. The server may return fewer than
      `max_alternatives`. Valid values are `0`-`30`. A value of `0` or `1`
      will return a maximum of one. If omitted, will return a maximum of one.
    profanityFilter: *Optional* If set to `true`, the server will attempt to
      filter out profanities, replacing all but the initial character in each
      filtered word with asterisks, e.g. "f***". If set to `false` or omitted,
      profanities won't be filtered out.
    sampleRateHertz: Sample rate in Hertz of the audio data sent in all
      `RecognitionAudio` messages. Valid values are: 8000-48000. 16000 is
      optimal. For best results, set the sampling rate of the audio source to
      16000 Hz. If that's not possible, use the native sample rate of the
      audio source (instead of re-sampling). This field is optional for `FLAC`
      and `WAV` audio files and required for all other audio formats. For
      details, see AudioEncoding.
    speechContexts: *Optional* A means to provide context to assist the speech
      recognition.
  """

  class EncodingValueValuesEnum(_messages.Enum):
    """Encoding of audio data sent in all `RecognitionAudio` messages. This
    field is optional for `FLAC` and `WAV` audio files and required for all
    other audio formats. For details, see AudioEncoding.

    Values:
      ENCODING_UNSPECIFIED: Not specified.
      LINEAR16: Uncompressed 16-bit signed little-endian samples (Linear PCM).
      FLAC: `FLAC` (Free Lossless Audio Codec) is the recommended encoding
        because it is lossless--therefore recognition is not compromised--and
        requires only about half the bandwidth of `LINEAR16`. `FLAC` stream
        encoding supports 16-bit and 24-bit samples, however, not all fields
        in `STREAMINFO` are supported.
      MULAW: 8-bit samples that compand 14-bit audio samples using G.711 PCMU
        /mu-law.
      AMR: Adaptive Multi-Rate Narrowband codec. `sample_rate_hertz` must be
        8000.
      AMR_WB: Adaptive Multi-Rate Wideband codec. `sample_rate_hertz` must be
        16000.
      OGG_OPUS: Opus encoded audio frames in Ogg container
        ([OggOpus](https://wiki.xiph.org/OggOpus)). `sample_rate_hertz` must
        be one of 8000, 12000, 16000, 24000, or 48000.
      SPEEX_WITH_HEADER_BYTE: Although the use of lossy encodings is not
        recommended, if a very low bitrate encoding is required, `OGG_OPUS` is
        highly preferred over Speex encoding. The [Speex](https://speex.org/)
        encoding supported by Cloud Speech API has a header byte in each
        block, as in MIME type `audio/x-speex-with-header-byte`. It is a
        variant of the RTP Speex encoding defined in [RFC
        5574](https://tools.ietf.org/html/rfc5574). The stream is a sequence
        of blocks, one block per RTP packet. Each block starts with a byte
        containing the length of the block, in bytes, followed by one or more
        frames of Speex data, padded to an integral number of bytes (octets)
        as specified in RFC 5574. In other words, each RTP header is replaced
        with a single byte containing the block length. Only Speex wideband is
        supported. `sample_rate_hertz` must be 16000.
    """
    ENCODING_UNSPECIFIED = 0
    LINEAR16 = 1
    FLAC = 2
    MULAW = 3
    AMR = 4
    AMR_WB = 5
    OGG_OPUS = 6
    SPEEX_WITH_HEADER_BYTE = 7

  enableWordTimeOffsets = _messages.BooleanField(1)
  encoding = _messages.EnumField('EncodingValueValuesEnum', 2)
  languageCode = _messages.StringField(3)
  maxAlternatives = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  profanityFilter = _messages.BooleanField(5)
  sampleRateHertz = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  speechContexts = _messages.MessageField('SpeechContext', 7, repeated=True)


class RecognizeRequest(_messages.Message):
  """The top-level message sent by the client for the `Recognize` method.

  Fields:
    audio: *Required* The audio data to be recognized.
    config: *Required* Provides information to the recognizer that specifies
      how to process the request.
  """

  audio = _messages.MessageField('RecognitionAudio', 1)
  config = _messages.MessageField('RecognitionConfig', 2)


class RecognizeResponse(_messages.Message):
  """The only message returned to the client by the `Recognize` method. It
  contains the result as zero or more sequential `SpeechRecognitionResult`
  messages.

  Fields:
    results: Output only. Sequential list of transcription results
      corresponding to sequential portions of audio.
  """

  results = _messages.MessageField('SpeechRecognitionResult', 1, repeated=True)


class SpeechContext(_messages.Message):
  """Provides "hints" to the speech recognizer to favor specific words and
  phrases in the results.

  Fields:
    phrases: *Optional* A list of strings containing words and phrases "hints"
      so that the speech recognition is more likely to recognize them. This
      can be used to improve the accuracy for specific words and phrases, for
      example, if specific commands are typically spoken by the user. This can
      also be used to add additional words to the vocabulary of the
      recognizer. See [usage
      limits](https://cloud.google.com/speech/limits#content).
  """

  phrases = _messages.StringField(1, repeated=True)


class SpeechOperationsGetRequest(_messages.Message):
  """A SpeechOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class SpeechRecognitionAlternative(_messages.Message):
  """Alternative hypotheses (a.k.a. n-best list).

  Fields:
    confidence: Output only. The confidence estimate between 0.0 and 1.0. A
      higher number indicates an estimated greater likelihood that the
      recognized words are correct. This field is set only for the top
      alternative of a non-streaming result or, of a streaming result where
      `is_final=true`. This field is not guaranteed to be accurate and users
      should not rely on it to be always provided. The default of 0.0 is a
      sentinel value indicating `confidence` was not set.
    transcript: Output only. Transcript text representing the words that the
      user spoke.
    words: Output only. A list of word-specific information for each
      recognized word. Note: When enable_speaker_diarization is true, you will
      see all the words from the beginning of the audio.
  """

  confidence = _messages.FloatField(1, variant=_messages.Variant.FLOAT)
  transcript = _messages.StringField(2)
  words = _messages.MessageField('WordInfo', 3, repeated=True)


class SpeechRecognitionResult(_messages.Message):
  """A speech recognition result corresponding to a portion of the audio.

  Fields:
    alternatives: Output only. May contain one or more recognition hypotheses
      (up to the maximum specified in `max_alternatives`). These alternatives
      are ordered in terms of accuracy, with the top (first) alternative being
      the most probable, as ranked by the recognizer.
  """

  alternatives = _messages.MessageField('SpeechRecognitionAlternative', 1, repeated=True)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
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
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class Status(_messages.Message):
  """The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class WordInfo(_messages.Message):
  """Word-specific information for recognized words.

  Fields:
    endTime: Output only. Time offset relative to the beginning of the audio,
      and corresponding to the end of the spoken word. This field is only set
      if `enable_word_time_offsets=true` and only in the top hypothesis. This
      is an experimental feature and the accuracy of the time offset can vary.
    speakerTag: Output only. A distinct integer value is assigned for every
      speaker within the audio. This field specifies which one of those
      speakers was detected to have spoken this word. Value ranges from '1' to
      diarization_speaker_count. speaker_tag is set if
      enable_speaker_diarization = 'true' and only in the top alternative.
    startTime: Output only. Time offset relative to the beginning of the
      audio, and corresponding to the start of the spoken word. This field is
      only set if `enable_word_time_offsets=true` and only in the top
      hypothesis. This is an experimental feature and the accuracy of the time
      offset can vary.
    word: Output only. The word corresponding to this set of information.
  """

  endTime = _messages.StringField(1)
  speakerTag = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  startTime = _messages.StringField(3)
  word = _messages.StringField(4)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
