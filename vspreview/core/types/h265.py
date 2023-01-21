'''[ITU-T H.265](https://www.itu.int/rec/T-REC-H.265)'''
from enum import IntEnum

import vapoursynth as vs


class ColorRange(IntEnum):

    FULL = 0
    LIMITED = 1


class ChromaLocation(IntEnum):
    '''Figure E.2 – Location of the top-left chroma sample when chroma_format_idc is equal to 1 (4:2:0 chroma format) as a function of ChromaLocType'''

    LEFT = 0
    CENTER = 1
    TOP_LEFT = 2
    TOP = 3
    BOTTOM_LEFT = 4
    BOTTOM = 5


class FieldBased(IntEnum):

    PROGRESSIVE = 0
    BOTTOM_FIELD_FIRST = 1
    TOP_FIELD_FIRST = 2


class Primaries(IntEnum):
    '''Table E.3 – Colour primaries interpretation using the colour_primaries syntax element'''

    BT709 = 1
    '''
    Rec. ITU-R BT.709-6\n
    Rec. ITU-R BT.1361-0 conventional colour gamut system and extended colour gamut system (historical)\n
    IEC 61966-2-1 sRGB or sYCC\n
    IEC 61966-2-4\n
    SMPTE RP 177 (1993) Annex B
    '''

    UNSPECIFIED = 2
    '''
    Image characteristics are unknown or are determined by the application.
    '''

    BT470M = 4
    '''
    Rec. ITU-R BT.470-6 System M (historical)\n
    NTSC Recommendation for transmission standards for colour television (1953)\n
    FCC Title 47 Code of Federal Regulations (2003) 73.682 (a) (20)
    '''

    BT470BG = 5
    '''
    Rec. ITU-R BT.470-6 System B, G (historical)\n
    Rec. ITU-R BT.601-7 625\n
    Rec. ITU-R BT.1358-0 625 (historical)\n
    Rec. ITU-R BT.1700-0 625 PAL and 625\n
    SECAM
    '''

    BT601 = 6
    '''
    Rec. ITU-R BT.601-7 525\n
    Rec. ITU-R BT.1358-1 525 or 625 (historical)\n
    Rec. ITU-R BT.1700-0 NTSC\n
    SMPTE ST 170 (2004)\n
    (functionally the same as the value 7)
    '''

    ST240 = 7
    '''
    SMPTE ST 240 (1999, historical)\n
    (functionally the same as the value 6)
    '''

    FILM = 8
    '''
    Generic film (colour filters using Illuminant C)
    '''

    BT2020 = 9
    '''
    Rec. ITU-R BT.2020-2\n
    Rec. ITU-R BT.2100-2
    '''

    ST428 = 10
    '''
    SMPTE ST 428-1 (2006)\n
    (CIE 1931 XYZ)
    '''

    P3DCI = 11
    '''
    SMPTE RP 431-2 (2011)\n
    SMPTE ST 2113 (2019) "P3DCI"
    '''

    P3D65 = 12
    '''
    SMPTE EG 432-1 (2010)
    SMPTE ST 2113 (2019) "P3D65"
    '''

    EBU3213 = 22
    '''EBU Tech. 3213-E (1975)'''


class Transfer(IntEnum):
    '''Table E.4 – Transfer characteristics interpretation using the transfer_characteristics syntax element'''

    BT709 = 1
    '''
    Rec. ITU-R BT.709-6\n
    Rec. ITU-R BT.1361-0 conventional colour gamut system (historical)\n
    (functionally the same as the values 6, 14, and 15)
    '''

    UNSPECIFIED = 2
    '''
    Image characteristics are unknown or are determined by the application.
    '''

    BT470M = 4
    '''
    Assumed display gamma 2.2\n
    Rec. ITU-R BT.470-6 System M (historical)\n
    NTSC Recommendation for transmission standards for colour television (1953)\n
    FCC, Title 47 Code of Federal Regulations (2003) 73.682 (a) (20)
    '''

    BT470BG = 5
    '''
    Assumed display gamma 2.8\n
    Rec. ITU-R BT.601-7 525 or 625\n
    Rec. ITU-R BT.1358-1 525 or 625 (historical)\n
    Rec. ITU-R BT.1700-0 NTSC\n
    SMPTE ST 170 (2004)\n
    (functionally the same as the values 1, 14, and 15)
    '''

    BT601 = 6
    '''
    Rec. ITU-R BT.601-7 525 or 625\n
    Rec. ITU-R BT.1358-1 525 or 625 (historical)\n
    Rec. ITU-R BT.1700-0\n
    NTSC SMPTE ST 170 (2004)\n
    (functionally the same as the values 1, 14, and 15)
    '''

    ST240 = 7
    '''
    SMPTE ST 240 (1999, historical)
    '''

    LINEAR = 8
    '''
    Linear transfer characteristics
    '''

    LOG100 = 9
    '''
    Logarithmic transfer characteristic (100:1 range)
    '''

    LOG316 = 10
    '''
    Logarithmic transfer characteristic (100 * Sqrt( 10 ) : 1 range)
    '''

    XVYCC = 11
    '''
    IEC 61966-2-4
    '''

    BT1361 = 12
    '''
    Rec. ITU-R BT.1361-0 extended colour gamut system (historical)
    '''

    SRGB = 13
    '''
    IEC 61966-2-1 sRGB (with matrix_coeffs equal to 0)\n
    IEC 61966-2-1 sYCC (with matrix_coeffs equal to 5)
    '''

    BT2020_10 = 14
    '''
    Rec. ITU-R BT.2020-2 (functionally the same as the values 1, 6, and 15)
    '''

    BT2020_12 = 15
    '''
    Rec. ITU-R BT.2020-2 (functionally the same as the values 1, 6, and 14)
    '''

    PQ = 16
    '''
    SMPTE ST 2084 (2014) for 10, 12, 14, and 16-bit systems\n
    Rec. ITU-R BT.2100-2 perceptual quantization (PQ) system
    '''

    ST428 = 17
    '''
    SMPTE ST 428-1 (2006)
    '''

    HLG = 18
    '''
    Association of Radio Industries and Businesses (ARIB) STD-B67\n
    Rec. ITU-R BT.2100-2 hybrid log- gamma (HLG) system
    '''


class Matrix(IntEnum):
    '''Table E.5 – Matrix coefficients interpretation using the matrix_coeffs syntax element'''

    RGB = 0
    '''
    The identity matrix.\n
    Typically used for GBR (often referred to as RGB); however, may also be used for YZX (often referred to as XYZ)\n
    IEC 61966-2-1 sRGB\n
    SMPTE ST 428-1 (2006)\n
    See Equations E-31 to E-33\n
    '''

    BT709 = 1
    '''
    Rec. ITU-R BT.709-6\n
    Rec. ITU-R BT.1361-0 conventional colour gamut system and extended colour gamut system (historical)\n
    IEC 61966-2-4 xvYCC_709\n
    SMPTE RP 177 (1993) Annex B\n
    See Equations E-28 to E-30\n
    '''

    UNSPECIFIED = 2
    '''
    Image characteristics are unknown or are determined by the application.
    '''

    BT470M = 4
    '''
    FCC Title 47 Code of Federal Regulations (2003) 73.682 (a) (20)\n
    See Equations E-28 to E-30
    '''

    BT470BG = 5
    '''
    Rec. ITU-R BT.470-6 System B, G (historical)\n
    Rec. ITU-R BT.601-7 625\n
    Rec. ITU-R BT.1358-0 625 (historical)\n
    Rec. ITU-R BT.1700-0 625 PAL and 625 SECAM\n
    IEC 61966-2-1 sYCC\n
    IEC 61966-2-4 xvYCC601\n
    (functionally the same as the value 6)\n
    See Equations E-28 to E-30
    '''

    BT601 = 6
    '''
    Rec. ITU-R BT.601-7 525\n
    Rec. ITU-R BT.1358-1 525 or 625 (historical)\n
    Rec. ITU-R BT.1700-0 NTSC\n
    SMPTE ST 170 (2004)\n
    (functionally the same as the value 5)\n
    See Equations E-28 to E-30\n
    '''

    ST240 = 7
    '''
    SMPTE ST 240 (1999, historical)\n
    See Equations E-28 to E-30
    '''

    YCOCG = 8
    '''
    See Equations E-34 to E-48
    '''

    BT2020 = 9
    '''
    Rec. ITU-R BT.2020-2 non-constant luminance system\n
    Rec. ITU-R BT.2100-2 Y′CbCr\n
    See Equations E-28 to E-30
    '''

    BT2020_CL = 10
    '''
    Rec. ITU-R BT.2020-2 constant luminance system\n
    See Equations E-49 to E-58
    '''

    YDZDX = 11
    '''
    SMPTE ST 2085 (2015)\n
    See Equations E-59 to E-61
    '''

    CHROMATIC = 12
    '''
    Chromaticity-derived non-constant luminance system\n
    See Equations E-28 to E-30
    '''

    CHROMATIC_CL = 13
    '''
    Chromaticity-derived constant luminance system\n
    See Equations E-49 to E-58
    '''

    ICTCP = 14
    '''
    Rec. ITU-R BT.2100-2 ICTCP\n
    See Equations E-62 to E-64 for transfer_characteristics value 16 (PQ)\n
    See Equations E-65 to E-67 for transfer_characteristics value 18 (HLG)
    '''


def video_heuristics(clip: vs.VideoNode, props: vs.FrameProps | None = None) -> dict[str, int]:
    def from_res(clip: vs.VideoNode):
        video_format, width, height = clip.format, clip.width, clip.height
        if not (video_format and width and height):
            frame = clip.get_frame(0)
            video_format, width, height = frame.format, frame.width, frame.height

        if width <= 1024 and height <= 576:
            if height == 576:
                matrix = Matrix.BT470BG
                primaries = Primaries.BT470BG
                transfer = Transfer.BT470BG
            else:
                matrix = Matrix.BT601
                primaries = Primaries.BT601
                transfer = Transfer.BT601
        elif width <= 2048 and height <= 1536:
            matrix = Matrix.BT709
            primaries = Primaries.BT709
            transfer = Transfer.BT709
        else:
            matrix = Matrix.BT2020
            primaries = Primaries.BT2020
            transfer = Transfer.PQ
        color_range = ColorRange.LIMITED

        if video_format.color_family == vs.RGB:
            matrix = Matrix.RGB
            primaries = Primaries.BT709
            transfer = Transfer.SRGB
            color_range = ColorRange.FULL

        return matrix, primaries, transfer, color_range

    def from_video(clip: vs.VideoNode):
        matrix, primaries, transfer, color_range = from_res(clip)
        props = clip.props
        matrix = Matrix(int(props['_Matrix'])) if '_Matrix' in props else matrix
        primaries = Primaries(int(props['_Primaries'])) if '_Primaries' in props else primaries
        transfer = Transfer(int(props['_Transfer'])) if '_Transfer' in props else transfer
        color_range = ColorRange(int(props['_ColorRange'])) if '_ColorRange' in props else color_range
        return matrix, primaries, transfer, color_range

    if props:
        matrix, primaries, transfer, color_range = from_video(clip)
    else:
        matrix, primaries, transfer, color_range = from_res(clip)

    heuristics = dict[str, IntEnum]()
    heuristics |= {
        'matrix': matrix, 'primaries': primaries, 'transfer': transfer, 'range': color_range
    }

    return {f'{k}_in': v for k, v in heuristics.items()}
