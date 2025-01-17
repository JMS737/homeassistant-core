"""Test Jellyfin diagnostics."""

from homeassistant.core import HomeAssistant

from tests.common import MockConfigEntry
from tests.components.diagnostics import get_diagnostics_for_config_entry
from tests.typing import ClientSessionGenerator


async def test_diagnostics(
    hass: HomeAssistant,
    init_integration: MockConfigEntry,
    hass_client: ClientSessionGenerator,
):
    """Test generating diagnostics for a config entry."""
    entry = init_integration

    diag = await get_diagnostics_for_config_entry(hass, hass_client, entry)
    assert diag
    assert diag["entry"] == {
        "title": "Jellyfin",
        "data": {
            "url": "https://example.com",
            "username": "test-username",
            "password": "**REDACTED**",
            "client_device_id": entry.entry_id,
        },
    }
    assert diag["server"] == {
        "id": "SERVER-UUID",
        "name": "JELLYFIN-SERVER",
        "version": None,
    }
    assert diag["sessions"]
    assert len(diag["sessions"]) == 4
    assert diag["sessions"][0] == {
        "id": "SESSION-UUID",
        "user_id": "08ba1929-681e-4b24-929b-9245852f65c0",
        "device_id": "DEVICE-UUID",
        "device_name": "JELLYFIN-DEVICE",
        "client_name": "Jellyfin for Developers",
        "client_version": "1.0.0",
        "capabilities": {
            "PlayableMediaTypes": ["Video"],
            "SupportedCommands": ["VolumeSet", "Mute"],
            "SupportsMediaControl": True,
            "SupportsContentUploading": True,
            "MessageCallbackUrl": "string",
            "SupportsPersistentIdentifier": True,
            "SupportsSync": True,
            "DeviceProfile": {
                "Name": "string",
                "Id": "string",
                "Identification": {
                    "FriendlyName": "string",
                    "ModelNumber": "string",
                    "SerialNumber": "string",
                    "ModelName": "string",
                    "ModelDescription": "string",
                    "ModelUrl": "string",
                    "Manufacturer": "string",
                    "ManufacturerUrl": "string",
                    "Headers": [
                        {"Name": "string", "Value": "string", "Match": "Equals"}
                    ],
                },
                "FriendlyName": "string",
                "Manufacturer": "string",
                "ManufacturerUrl": "string",
                "ModelName": "string",
                "ModelDescription": "string",
                "ModelNumber": "string",
                "ModelUrl": "string",
                "SerialNumber": "string",
                "EnableAlbumArtInDidl": False,
                "EnableSingleAlbumArtLimit": False,
                "EnableSingleSubtitleLimit": False,
                "SupportedMediaTypes": "string",
                "UserId": "string",
                "AlbumArtPn": "string",
                "MaxAlbumArtWidth": 0,
                "MaxAlbumArtHeight": 0,
                "MaxIconWidth": 0,
                "MaxIconHeight": 0,
                "MaxStreamingBitrate": 0,
                "MaxStaticBitrate": 0,
                "MusicStreamingTranscodingBitrate": 0,
                "MaxStaticMusicBitrate": 0,
                "SonyAggregationFlags": "string",
                "ProtocolInfo": "string",
                "TimelineOffsetSeconds": 0,
                "RequiresPlainVideoItems": False,
                "RequiresPlainFolders": False,
                "EnableMSMediaReceiverRegistrar": False,
                "IgnoreTranscodeByteRangeRequests": False,
                "XmlRootAttributes": [{"Name": "string", "Value": "string"}],
                "DirectPlayProfiles": [
                    {
                        "Container": "string",
                        "AudioCodec": "string",
                        "VideoCodec": "string",
                        "Type": "Audio",
                    }
                ],
                "TranscodingProfiles": [
                    {
                        "Container": "string",
                        "Type": "Audio",
                        "VideoCodec": "string",
                        "AudioCodec": "string",
                        "Protocol": "string",
                        "EstimateContentLength": False,
                        "EnableMpegtsM2TsMode": False,
                        "TranscodeSeekInfo": "Auto",
                        "CopyTimestamps": False,
                        "Context": "Streaming",
                        "EnableSubtitlesInManifest": False,
                        "MaxAudioChannels": "string",
                        "MinSegments": 0,
                        "SegmentLength": 0,
                        "BreakOnNonKeyFrames": False,
                        "Conditions": [
                            {
                                "Condition": "Equals",
                                "Property": "AudioChannels",
                                "Value": "string",
                                "IsRequired": True,
                            }
                        ],
                    }
                ],
                "ContainerProfiles": [
                    {
                        "Type": "Audio",
                        "Conditions": [
                            {
                                "Condition": "Equals",
                                "Property": "AudioChannels",
                                "Value": "string",
                                "IsRequired": True,
                            }
                        ],
                        "Container": "string",
                    }
                ],
                "CodecProfiles": [
                    {
                        "Type": "Video",
                        "Conditions": [
                            {
                                "Condition": "Equals",
                                "Property": "AudioChannels",
                                "Value": "string",
                                "IsRequired": True,
                            }
                        ],
                        "ApplyConditions": [
                            {
                                "Condition": "Equals",
                                "Property": "AudioChannels",
                                "Value": "string",
                                "IsRequired": True,
                            }
                        ],
                        "Codec": "string",
                        "Container": "string",
                    }
                ],
                "ResponseProfiles": [
                    {
                        "Container": "string",
                        "AudioCodec": "string",
                        "VideoCodec": "string",
                        "Type": "Audio",
                        "OrgPn": "string",
                        "MimeType": "string",
                        "Conditions": [
                            {
                                "Condition": "Equals",
                                "Property": "AudioChannels",
                                "Value": "string",
                                "IsRequired": True,
                            }
                        ],
                    }
                ],
                "SubtitleProfiles": [
                    {
                        "Format": "string",
                        "Method": "Encode",
                        "DidlMode": "string",
                        "Language": "string",
                        "Container": "string",
                    }
                ],
            },
            "AppStoreUrl": "string",
            "IconUrl": "string",
        },
        "now_playing": {
            "Name": "EPISODE",
            "OriginalTitle": "string",
            "ServerId": "SERVER-UUID",
            "Id": "EPISODE-UUID",
            "Etag": "string",
            "SourceType": "string",
            "PlaylistItemId": "string",
            "DateCreated": "2019-08-24T14:15:22Z",
            "DateLastMediaAdded": "2019-08-24T14:15:22Z",
            "ExtraType": "string",
            "AirsBeforeSeasonNumber": 0,
            "AirsAfterSeasonNumber": 0,
            "AirsBeforeEpisodeNumber": 0,
            "CanDelete": True,
            "CanDownload": True,
            "HasSubtitles": True,
            "PreferredMetadataLanguage": "string",
            "PreferredMetadataCountryCode": "string",
            "SupportsSync": True,
            "Container": "string",
            "SortName": "string",
            "ForcedSortName": "string",
            "Video3DFormat": "HalfSideBySide",
            "PremiereDate": "2019-08-24T14:15:22Z",
            "ExternalUrls": [{"Name": "string", "Url": "string"}],
            "MediaSources": [
                {
                    "Protocol": "File",
                    "Id": "string",
                    "Path": "string",
                    "EncoderPath": "string",
                    "EncoderProtocol": "File",
                    "Type": "Default",
                    "Container": "string",
                    "Size": 0,
                    "Name": "string",
                    "IsRemote": True,
                    "ETag": "string",
                    "RunTimeTicks": 0,
                    "ReadAtNativeFramerate": True,
                    "IgnoreDts": True,
                    "IgnoreIndex": True,
                    "GenPtsInput": True,
                    "SupportsTranscoding": True,
                    "SupportsDirectStream": True,
                    "SupportsDirectPlay": True,
                    "IsInfiniteStream": True,
                    "RequiresOpening": True,
                    "OpenToken": "string",
                    "RequiresClosing": True,
                    "LiveStreamId": "string",
                    "BufferMs": 0,
                    "RequiresLooping": True,
                    "SupportsProbing": True,
                    "VideoType": "VideoFile",
                    "IsoType": "Dvd",
                    "Video3DFormat": "HalfSideBySide",
                    "MediaStreams": [
                        {
                            "Codec": "string",
                            "CodecTag": "string",
                            "Language": "string",
                            "ColorRange": "string",
                            "ColorSpace": "string",
                            "ColorTransfer": "string",
                            "ColorPrimaries": "string",
                            "DvVersionMajor": 0,
                            "DvVersionMinor": 0,
                            "DvProfile": 0,
                            "DvLevel": 0,
                            "RpuPresentFlag": 0,
                            "ElPresentFlag": 0,
                            "BlPresentFlag": 0,
                            "DvBlSignalCompatibilityId": 0,
                            "Comment": "string",
                            "TimeBase": "string",
                            "CodecTimeBase": "string",
                            "Title": "string",
                            "VideoRange": "string",
                            "VideoRangeType": "string",
                            "VideoDoViTitle": "string",
                            "LocalizedUndefined": "string",
                            "LocalizedDefault": "string",
                            "LocalizedForced": "string",
                            "LocalizedExternal": "string",
                            "DisplayTitle": "string",
                            "NalLengthSize": "string",
                            "IsInterlaced": True,
                            "IsAVC": True,
                            "ChannelLayout": "string",
                            "BitRate": 0,
                            "BitDepth": 0,
                            "RefFrames": 0,
                            "PacketLength": 0,
                            "Channels": 0,
                            "SampleRate": 0,
                            "IsDefault": True,
                            "IsForced": True,
                            "Height": 0,
                            "Width": 0,
                            "AverageFrameRate": 0,
                            "RealFrameRate": 0,
                            "Profile": "string",
                            "Type": "Audio",
                            "AspectRatio": "string",
                            "Index": 0,
                            "Score": 0,
                            "IsExternal": True,
                            "DeliveryMethod": "Encode",
                            "DeliveryUrl": "string",
                            "IsExternalUrl": True,
                            "IsTextSubtitleStream": True,
                            "SupportsExternalStream": True,
                            "Path": "string",
                            "PixelFormat": "string",
                            "Level": 0,
                            "IsAnamorphic": True,
                        }
                    ],
                    "MediaAttachments": [
                        {
                            "Codec": "string",
                            "CodecTag": "string",
                            "Comment": "string",
                            "Index": 0,
                            "FileName": "string",
                            "MimeType": "string",
                            "DeliveryUrl": "string",
                        }
                    ],
                    "Formats": ["string"],
                    "Bitrate": 0,
                    "Timestamp": "None",
                    "RequiredHttpHeaders": {
                        "property1": "string",
                        "property2": "string",
                    },
                    "TranscodingUrl": "string",
                    "TranscodingSubProtocol": "string",
                    "TranscodingContainer": "string",
                    "AnalyzeDurationMs": 0,
                    "DefaultAudioStreamIndex": 0,
                    "DefaultSubtitleStreamIndex": 0,
                }
            ],
            "CriticRating": 0,
            "ProductionLocations": ["string"],
            "Path": "string",
            "EnableMediaSourceDisplay": True,
            "OfficialRating": "string",
            "CustomRating": "string",
            "ChannelId": "04b0b2a5-93cb-474d-8ea9-3df0f84eb0ff",
            "ChannelName": "string",
            "Overview": "string",
            "Taglines": ["string"],
            "Genres": ["string"],
            "CommunityRating": 0,
            "CumulativeRunTimeTicks": 0,
            "RunTimeTicks": 600000000,
            "PlayAccess": "Full",
            "AspectRatio": "string",
            "ProductionYear": 0,
            "IsPlaceHolder": True,
            "Number": "string",
            "ChannelNumber": "string",
            "IndexNumber": 3,
            "IndexNumberEnd": 0,
            "ParentIndexNumber": 1,
            "RemoteTrailers": [{"Url": "string", "Name": "string"}],
            "ProviderIds": {"property1": "string", "property2": "string"},
            "IsHD": True,
            "IsFolder": False,
            "ParentId": "PARENT-UUID",
            "Type": "Episode",
            "People": [
                {
                    "Name": "string",
                    "Id": "38a5a5bb-dc30-49a2-b175-1de0d1488c43",
                    "Role": "string",
                    "Type": "string",
                    "PrimaryImageTag": "string",
                    "ImageBlurHashes": {
                        "Primary": {"property1": "string", "property2": "string"},
                        "Art": {"property1": "string", "property2": "string"},
                        "Backdrop": {"property1": "string", "property2": "string"},
                        "Banner": {"property1": "string", "property2": "string"},
                        "Logo": {"property1": "string", "property2": "string"},
                        "Thumb": {"property1": "string", "property2": "string"},
                        "Disc": {"property1": "string", "property2": "string"},
                        "Box": {"property1": "string", "property2": "string"},
                        "Screenshot": {"property1": "string", "property2": "string"},
                        "Menu": {"property1": "string", "property2": "string"},
                        "Chapter": {"property1": "string", "property2": "string"},
                        "BoxRear": {"property1": "string", "property2": "string"},
                        "Profile": {"property1": "string", "property2": "string"},
                    },
                }
            ],
            "Studios": [
                {"Name": "string", "Id": "38a5a5bb-dc30-49a2-b175-1de0d1488c43"}
            ],
            "GenreItems": [
                {"Name": "string", "Id": "38a5a5bb-dc30-49a2-b175-1de0d1488c43"}
            ],
            "ParentLogoItemId": "c78d400f-de5c-421e-8714-4fb05d387233",
            "ParentBackdropItemId": "c22fd826-17fc-44f4-9b04-1eb3e8fb9173",
            "ParentBackdropImageTags": ["string"],
            "LocalTrailerCount": 0,
            "UserData": {
                "Rating": 0,
                "PlayedPercentage": 0,
                "UnplayedItemCount": 0,
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": True,
                "Likes": True,
                "LastPlayedDate": "2019-08-24T14:15:22Z",
                "Played": True,
                "Key": "string",
                "ItemId": "string",
            },
            "RecursiveItemCount": 0,
            "ChildCount": 0,
            "SeriesName": "SERIES",
            "SeriesId": "SERIES-UUID",
            "SeasonId": "SEASON-UUID",
            "SpecialFeatureCount": 0,
            "DisplayPreferencesId": "string",
            "Status": "string",
            "AirTime": "string",
            "AirDays": ["Sunday"],
            "Tags": ["string"],
            "PrimaryImageAspectRatio": 0,
            "Artists": ["string"],
            "ArtistItems": [
                {"Name": "string", "Id": "38a5a5bb-dc30-49a2-b175-1de0d1488c43"}
            ],
            "Album": "string",
            "CollectionType": "string",
            "DisplayOrder": "string",
            "AlbumId": "21af9851-8e39-43a9-9c47-513d3b9e99fc",
            "AlbumPrimaryImageTag": "string",
            "SeriesPrimaryImageTag": "string",
            "AlbumArtist": "string",
            "AlbumArtists": [
                {"Name": "string", "Id": "38a5a5bb-dc30-49a2-b175-1de0d1488c43"}
            ],
            "SeasonName": "SEASON",
            "MediaStreams": [
                {
                    "Codec": "string",
                    "CodecTag": "string",
                    "Language": "string",
                    "ColorRange": "string",
                    "ColorSpace": "string",
                    "ColorTransfer": "string",
                    "ColorPrimaries": "string",
                    "DvVersionMajor": 0,
                    "DvVersionMinor": 0,
                    "DvProfile": 0,
                    "DvLevel": 0,
                    "RpuPresentFlag": 0,
                    "ElPresentFlag": 0,
                    "BlPresentFlag": 0,
                    "DvBlSignalCompatibilityId": 0,
                    "Comment": "string",
                    "TimeBase": "string",
                    "CodecTimeBase": "string",
                    "Title": "string",
                    "VideoRange": "string",
                    "VideoRangeType": "string",
                    "VideoDoViTitle": "string",
                    "LocalizedUndefined": "string",
                    "LocalizedDefault": "string",
                    "LocalizedForced": "string",
                    "LocalizedExternal": "string",
                    "DisplayTitle": "string",
                    "NalLengthSize": "string",
                    "IsInterlaced": True,
                    "IsAVC": True,
                    "ChannelLayout": "string",
                    "BitRate": 0,
                    "BitDepth": 0,
                    "RefFrames": 0,
                    "PacketLength": 0,
                    "Channels": 0,
                    "SampleRate": 0,
                    "IsDefault": True,
                    "IsForced": True,
                    "Height": 0,
                    "Width": 0,
                    "AverageFrameRate": 0,
                    "RealFrameRate": 0,
                    "Profile": "string",
                    "Type": "Audio",
                    "AspectRatio": "string",
                    "Index": 0,
                    "Score": 0,
                    "IsExternal": True,
                    "DeliveryMethod": "Encode",
                    "DeliveryUrl": "string",
                    "IsExternalUrl": True,
                    "IsTextSubtitleStream": True,
                    "SupportsExternalStream": True,
                    "Path": "string",
                    "PixelFormat": "string",
                    "Level": 0,
                    "IsAnamorphic": True,
                }
            ],
            "VideoType": "VideoFile",
            "PartCount": 0,
            "MediaSourceCount": 0,
            "ImageTags": {"property1": "string", "property2": "string"},
            "BackdropImageTags": ["string"],
            "ScreenshotImageTags": ["string"],
            "ParentLogoImageTag": "string",
            "ParentArtItemId": "10c1875b-b82c-48e8-bae9-939a5e68dc2f",
            "ParentArtImageTag": "string",
            "SeriesThumbImageTag": "string",
            "ImageBlurHashes": {
                "Primary": {"property1": "string", "property2": "string"},
                "Art": {"property1": "string", "property2": "string"},
                "Backdrop": {"property1": "string", "property2": "string"},
                "Banner": {"property1": "string", "property2": "string"},
                "Logo": {"property1": "string", "property2": "string"},
                "Thumb": {"property1": "string", "property2": "string"},
                "Disc": {"property1": "string", "property2": "string"},
                "Box": {"property1": "string", "property2": "string"},
                "Screenshot": {"property1": "string", "property2": "string"},
                "Menu": {"property1": "string", "property2": "string"},
                "Chapter": {"property1": "string", "property2": "string"},
                "BoxRear": {"property1": "string", "property2": "string"},
                "Profile": {"property1": "string", "property2": "string"},
            },
            "SeriesStudio": "HASS",
            "ParentThumbItemId": "ae6ff707-333d-4994-be6d-b83ca1b35f46",
            "ParentThumbImageTag": "string",
            "ParentPrimaryImageItemId": "string",
            "ParentPrimaryImageTag": "string",
            "Chapters": [
                {
                    "StartPositionTicks": 0,
                    "Name": "string",
                    "ImagePath": "string",
                    "ImageDateModified": "2019-08-24T14:15:22Z",
                    "ImageTag": "string",
                }
            ],
            "LocationType": "FileSystem",
            "IsoType": "Dvd",
            "MediaType": "string",
            "EndDate": "2019-08-24T14:15:22Z",
            "LockedFields": ["Cast"],
            "TrailerCount": 0,
            "MovieCount": 0,
            "SeriesCount": 0,
            "ProgramCount": 0,
            "EpisodeCount": 0,
            "SongCount": 0,
            "AlbumCount": 0,
            "ArtistCount": 0,
            "MusicVideoCount": 0,
            "LockData": True,
            "Width": 0,
            "Height": 0,
            "CameraMake": "string",
            "CameraModel": "string",
            "Software": "string",
            "ExposureTime": 0,
            "FocalLength": 0,
            "ImageOrientation": "TopLeft",
            "Aperture": 0,
            "ShutterSpeed": 0,
            "Latitude": 0,
            "Longitude": 0,
            "Altitude": 0,
            "IsoSpeedRating": 0,
            "SeriesTimerId": "string",
            "ProgramId": "string",
            "ChannelPrimaryImageTag": "string",
            "StartDate": "2019-08-24T14:15:22Z",
            "CompletionPercentage": 0,
            "IsRepeat": True,
            "EpisodeTitle": "string",
            "ChannelType": "TV",
            "Audio": "Mono",
            "IsMovie": True,
            "IsSports": True,
            "IsSeries": True,
            "IsLive": True,
            "IsNews": True,
            "IsKids": True,
            "IsPremiere": True,
            "TimerId": "string",
            "CurrentProgram": {},
        },
        "play_state": {
            "PositionTicks": 100000000,
            "CanSeek": True,
            "IsPaused": True,
            "IsMuted": True,
            "VolumeLevel": 0,
            "AudioStreamIndex": 0,
            "SubtitleStreamIndex": 0,
            "MediaSourceId": "string",
            "PlayMethod": "Transcode",
            "RepeatMode": "RepeatNone",
            "LiveStreamId": "string",
        },
    }
