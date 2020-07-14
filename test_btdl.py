import unittest

import re

from btdl import clean_file_name, check_m3u8_URL


class TestDownload(unittest.TestCase):
    def test_clean_file_name(self):
        # Remove special characters that don't work with windows file names
        self.assertEqual(clean_file_name("/\\:*?<>|"), "")
        # Check if it passes with characters on the ends
        self.assertEqual(clean_file_name("aaa[/\\:aaaa"), "aaa[aaaa")

    def test_check_m3u8_URL(self):
        self.assertEqual(
            check_m3u8_URL(
                "https://cdn02.brighttalk.com/core/asset/video/424398/ios/iphone/video_1594373401-3.m3u8"
            ),
            "https://cdn02.brighttalk.com/core/asset/video/424398/ios/iphone/video_1594373401-3.m3u8",
        )
        # Check if it works when missing the protocol
        self.assertEqual(
            check_m3u8_URL(
                "cdn02.brighttalk.com/core/asset/video/424398/ios/iphone/video_1594373401-3.m3u8"
            ),
            "https://cdn02.brighttalk.com/core/asset/video/424398/ios/iphone/video_1594373401-3.m3u8",
        )
        # Check if it correctly raises an error without .m3u8 ending
        self.assertRaises(
            TypeError,
            check_m3u8_URL,
            "https://cdn02.brighttalk.com/core/asset/video/424398/ios/iphone/video_1594373401-3",
        )


if __name__ == "__main__":
    unittest.main()
