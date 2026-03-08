package com.example.frontiercommoditytrader.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val FrontierColors = darkColorScheme(
    primary = Color(0xFFFFB74D),
    secondary = Color(0xFF90CAF9),
    tertiary = Color(0xFFA5D6A7),
    background = Color(0xFF0B1015),
    surface = Color(0xFF17202B),
    onPrimary = Color.Black,
    onBackground = Color.White,
    onSurface = Color.White,
)

@Composable
fun TheDopestDealsTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = FrontierColors,
        typography = Typography,
        content = content,
    )
}
