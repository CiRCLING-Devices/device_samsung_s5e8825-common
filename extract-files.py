#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.fixups_lib import (
    lib_fixup_vendorcompat,
    lib_fixups_user_type,
    libs_proto_3_9_1,
)

namespace_imports = [
    'device/samsung/s5e8825-common',
    'hardware/samsung',
    'hardware/samsung_slsi-linaro/exynos',
    'hardware/samsung_slsi-linaro/graphics',
    'hardware/samsung_slsi-linaro/interfaces',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    libs_proto_3_9_1: lib_fixup_vendorcompat,
    'libuuid': lib_fixup_vendor_suffix,
}  # fmt: skip

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/vendor.samsung.hardware.keymint-V1-ndk_platform.so': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so',
            'android.hardware.security.keymint-V4-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so',
            'android.hardware.security.secureclock-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so',
             'android.hardware.security.sharedsecret-V1-ndk.so')
        .add_needed('android.hardware.security.rkp-V3-ndk.so')
        .replace_needed('libcrypto.so', 'libcrypto-tm.so')
        .replace_needed('libssl.so', 'libssl-tm.so')
        .add_needed('libshim_crypto.so'),
    'vendor/etc/init/android.hardware.security.keymint-service.samsung.rc': blob_fixup()
        .regex_replace('android\\.hardware\\.security\\.keymint-service\n',
            'android.hardware.security.keymint-service.samsung\n'),
    'vendor/lib64/libsensorlistener.so': blob_fixup()
        .add_needed('libshim_sensorndkbridge.so'),
    (
        'vendor/lib/sensors.grip.so',
        'vendor/lib/sensors.inputvirtual.so',
        'vendor/lib/sensors.sensorhub.so',
        'vendor/lib64/sensors.grip.so',
        'vendor/lib64/sensors.inputvirtual.so',
        'vendor/lib64/sensors.sensorhub.so',
    ): blob_fixup()
        .remove_needed('libhidltransport.so')
        .add_needed('libutils-v32.so')
        .binary_regex_replace(b'_ZN7android6Thread3runEPKcim', b'_ZN7utils326Thread3runEPKcim'),
    (
        'vendor/lib/libaudioparamupdate.so',
        'vendor/lib/libaboxpcmdump.so',
        'vendor/lib/libaudioproxy2.so',
        'vendor/lib64/libaudioparamupdate.so',
        'vendor/lib64/libaboxpcmdump.so',
        'vendor/lib64/libaudioproxy2.so',
    ): blob_fixup()
        .add_needed('libaudioroute.s5e8825.so')
        .add_needed('libtinyalsa.s5e8825.so'),
    'vendor/lib/hw/audio.primary.s5e8825.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute.s5e8825.so')
        .replace_needed('libtinyalsa.so', 'libtinyalsa.s5e8825.so')
        .sig_replace('84 68 01 2C 0B D1 15 22 C1 F8',
                    '84 68 01 2C 00 BF 15 22 C1 F8')
        .sig_replace('B0 FA 80 F0 40 09 10 BD 00 BF',
                    'B0 FA 80 F0 01 20 10 BD 00 BF'),
    'vendor/lib64/hw/audio.primary.s5e8825.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute.s5e8825.so')
        .replace_needed('libtinyalsa.so', 'libtinyalsa.s5e8825.so')
        .sig_replace('E1 00 00 54 A9 02 80 52 29 80 01 B9 08 65 40 B9',
                    '1F 20 03 D5 A9 02 80 52 29 80 01 B9 08 65 40 B9')
        .sig_replace('E0 17 9F 1A FD 7B C2 A8 C0 03 5F D6',
                    '20 00 80 52 FD 7B C2 A8 C0 03 5F D6'),
    'vendor/lib64/libsec-ril.so': blob_fixup()
        .sig_replace('80 0E 40 F9 E1 03 16 AA 82 0C 80 52 E3 03 15 AA',
            '80 0E 40 F9 E1 03 16 AA 82 0C 80 52 03 00 80 D2'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .replace_needed('libprotobuf-cpp-lite-3.9.1.so', 'libprotobuf-cpp-full-3.9.1.so'),
    'vendor/lib64/libssl-tm.so': blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-tm.so'),
    'vendor/lib/soundfx/libswdap.so': blob_fixup()
        .sig_replace('30 46 88 47 07 46 30 68',
                     '30 46 88 47 01 27 30 68'),
    'vendor/lib64/libVendorSemTelephonyProps.so': blob_fixup()
        .binary_regex_replace(rb'persist\.ril\.supportNrModefromCp', b'vendor.ril.supportNrModefromCp\x00'),
}  # fmt: skip

module = ExtractUtilsModule(
    's5e8825-common',
    'samsung',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
