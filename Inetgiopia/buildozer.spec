[app]

title = Inetgiopia
package.name = inetgiopia
package.domain = org.kivy

source.include_exts = py,java,kv,png,atlas
android.add_src = service

requirements = python3,kivy,jnius,android

android.permissions = INTERNET, FOREGROUND_SERVICE, PACKAGE_USAGE_STATS, READ_CLIPBOARD

android.manifest.add_services = \
    <service android:name="org.kivy.inetgiopia.ClipboardMonitorService" \
             android:enabled="true" \
             android:exported="false" />
