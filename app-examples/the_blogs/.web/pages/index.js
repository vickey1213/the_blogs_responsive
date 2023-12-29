

import "focus-visible/dist/focus-visible"
import { Fragment, useContext } from "react"
import { EventLoopContext } from "/utils/context"
import { Event, isTrue } from "/utils/state"
import { Box, Divider, Flex, HStack, Image, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {
  const [addEvents, connectError] = useContext(EventLoopContext);

  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Fragment>
  <Box className={`py-2 sm:px-8 px-4 `} sx={{"height": "55px", "width": "100%"}}>
  <HStack alignItems={`center`} justifyContent={`space-between`}>
  <Link as={NextLink} href={`/`}>
  <Image src={`/logo_darkmode.svg`} sx={{"width": "120px"}}/>
</Link>
  <Box className={`gap-6 items-center text-sm lg:flex hidden`}>
  <Link as={NextLink} className={`py-1 px-2  rounded-md text-white hover:text-[#111113] hover:bg-[#EDEEF0]`} href={`/manifesto`} sx={{"fontSize": "14px", "color": "white", "_hover": {"textDecoration": "none"}}}>
  {`Manifesto`}
</Link>
  <Link as={NextLink} className={`py-1 px-2  rounded-md text-white hover:text-[#111113] hover:bg-[#EDEEF0]`} href={`https://github.com/dot-agent/nextpy/tree/main/docs`} sx={{"color": "white", "fontSize": "14px", "_hover": {"textDecoration": "none"}}}>
  {`Documentation`}
</Link>
  <Link as={NextLink} className={`py-1 px-2  rounded-md text-white hover:text-[#111113] hover:bg-[#EDEEF0]`} href={`https://discord.gg/w7fNkUsaWf`} sx={{"color": "white", "fontSize": "14px", "_hover": {"textDecoration": "none"}}}>
  {`Hackathon`}
</Link>
  <Link as={NextLink} className={`py-1 px-2  rounded-md text-white hover:text-[#111113] hover:bg-[#EDEEF0]`} href={`https://github.com/dot-agent/nextpy/tree/main/app-examples`} sx={{"color": "white", "fontSize": "14px", "_hover": {"textDecoration": "none"}}}>
  {`App Templates`}
</Link>
</Box>
  <Box className={`flex items-center flex-row gap-6`}>
  <Link as={NextLink} href={`https://github.com/dot-agent/nextpy`} sx={{"color": "#D0D1D3", "fontSize": "14px", "_hover": {"textDecoration": "none"}}}>
  {`Support`}
</Link>
  <Link as={NextLink} href={`https://discord.gg/g9PFpVztZg`} isExternal={true}>
  <Image src={`/discord.svg`} sx={{"width": "1.2rem"}}/>
</Link>
  <Link as={NextLink} href={`https://github.com/dot-agent/nextpy`} isExternal={true}>
  <Image src={`/github-mark.svg`} sx={{"width": "1.2rem"}}/>
</Link>
</Box>
</HStack>
</Box>
  <Box className={`flex justify-center text-center pb-10 `}>
  <Box className={`w-full lg:w-4/5 `}>
  <Divider sx={{"borderColor": "white"}}/>
  <Text className={`lg:text-9xl text-6xl md:text-[150px] font-bold pb-4 `}>
  {`THE BLOG`}
</Text>
  <Divider sx={{"borderColor": "white"}}/>
</Box>
</Box>
  <Box className={`flex flex-col gap-6 py-6 px-4 xl:px-48`}>
  <Box className={`grid grid-cols-1 md:grid-cols-1 lg:grid-cols-2 gap-6`}>
  <Box>
  <Box>
  <Box>
  <Image src={`Image.svg`}/>
  <Text className={`text-sm text-[#6941C6] pb-3 pt-6`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-3`}>
  {`UX review presentations`}
</Text>
  <Text className={`text-sm pb-6`}>
  {`How do you create compelling presentations that wow your colleagues and impress your managers?`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#6941C6] bg-white rounded-full px-4 py-2 items-center`}>
  {`Design`}
</Text>
  <Text className={`text-sm text-[#3538CD] bg-white rounded-full px-4 py-2 text-center`}>
  {`Research`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full px-4 py-2 text-center `}>
  {`Presentation`}
</Text>
</HStack>
</Box>
</Box>
</Box>
  <Box className={`grid grid-rows-2 gap-6`}>
  <Box>
  <Box className={`gap-4 flex flex-col md:justify-center md:flex-row justify-start items-start`}>
  <Box className={`flex-1`}>
  <Image className={`w-full h-full`} src={`Image (1).svg`}/>
</Box>
  <Box className={`flex-1`}>
  <Flex className={`flex flex-col items-start justify-start`}>
  <Text className={`text-sm text-[#6941C6] pb-3 `}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-3`}>
  {`Migrating to Linear 101`}
</Text>
  <Text className={`text-sm pb-6`}>
  {`Linear helps streamline software projects, sprints, tasks, and bug tracking. Here's how to get...`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#027A48] bg-white rounded-full px-4 py-2 items-center`}>
  {`Design`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full px-4 py-2 text-center`}>
  {`Research`}
</Text>
</HStack>
</Flex>
</Box>
</Box>
</Box>
  <Box>
  <Box className={`gap-4 flex flex-col md:justify-center md:flex-row justify-start items-start`}>
  <Box className={`flex-1`}>
  <Image className={`w-full h-full`} src={`Image (2).svg`}/>
</Box>
  <Box className={`flex-1`}>
  <Flex className={`flex flex-col items-start justify-start `}>
  <Text className={`text-sm text-[#6941C6] pb-4 pt-4`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-3`}>
  {`Building your API Stack`}
</Text>
  <Text className={`text-sm pb-4`}>
  {`The rise of RESTful APIs has been met by a rise in tools for creating, testing, and managing them.`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#6941C6] bg-white rounded-full px-4 py-2 items-center`}>
  {`Design`}
</Text>
  <Text className={`text-sm text-[#3538CD] bg-white rounded-full px-4 py-2 text-center`}>
  {`Research`}
</Text>
</HStack>
</Flex>
</Box>
</Box>
</Box>
</Box>
</Box>
  <Flex className={`flex items-center justify-center flex-col md:flex-row  h-[306] gap-6 `}>
  <Box className={`flex-1`}>
  <Image src={`Image (3).svg`} sx={{"width": "592px", "height": "246px"}}/>
</Box>
  <Box className={`flex-1`}>
  <Flex className={`flex flex-col items-start justify-start`}>
  <Text className={`text-sm text-[#6941C6] pb-4 pt-4`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-4`}>
  {`Grid system for better Design User Interface`}
</Text>
  <Text className={`text-sm pb-4`}>
  {`A grid system is a design tool used to arrange content on a webpage. It is a series of vertical and horizontal lines that create a matrix of intersecting points, which can be used to align and organize page elements. Grid systems are used to create a consistent look and feel across a website, and can help to make the layout more visually appealing and easier to navigate.`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#027A48] bg-white rounded-full px-4 py-2`}>
  {`Design`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full px-4 py-2 `}>
  {`Interface`}
</Text>
</HStack>
</Flex>
</Box>
</Flex>
  <Box className={`grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`}>
  <Box>
  <Box>
  <Image src={`Image (4).svg`} sx={{"width": "384px", "height": "240px"}}/>
  <Text className={`text-sm text-[#6941C6] pb-4 pt-4`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-4`}>
  {`Bill Walsh leadership lessons`}
</Text>
  <Text className={`text-sm pb-4`}>
  {`Like to know the secrets of transforming a 2-14 team into a 3x Super Bowl winning Dynasty?`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center`}>
  {`Leadership`}
</Text>
  <Text className={`text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center`}>
  {`Management`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center `}>
  {`Presentation`}
</Text>
</HStack>
</Box>
</Box>
  <Box>
  <Box>
  <Image src={`Image (5).svg`} sx={{"width": "384px", "height": "240px"}}/>
  <Text className={`text-sm text-[#6941C6] pb-4 pt-4`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-4`}>
  {`PM mental models`}
</Text>
  <Text className={`text-sm pb-4`}>
  {`Mental models are simple expressions of complex processes or relationships.`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center`}>
  {`Prodct`}
</Text>
  <Text className={`text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center`}>
  {`Reseach`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center `}>
  {`Framework`}
</Text>
</HStack>
</Box>
</Box>
  <Box>
  <Box>
  <Image src={`Image (6).svg`} sx={{"width": "384px", "height": "240px"}}/>
  <Text className={`text-sm text-[#6941C6] pb-4 pt-4`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-4`}>
  {`What is Wireframing?`}
</Text>
  <Text className={`text-sm pb-4`}>
  {`Introduction to Wireframing and its Principles. Learn from the best in the industry.`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center`}>
  {`Design`}
</Text>
  <Text className={`text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center`}>
  {`Reseach`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center `}>
  {`Presentation`}
</Text>
</HStack>
</Box>
</Box>
  <Box>
  <Box>
  <Image src={`Image (7).svg`} sx={{"width": "384px", "height": "240px"}}/>
  <Text className={`text-sm text-[#6941C6] pb-4 pt-4`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-4`}>
  {`How collaboration makes us better designers`}
</Text>
  <Text className={`text-sm pb-4`}>
  {`Collaboration can make our teams stronger, and our individual designs better.`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center`}>
  {`Design`}
</Text>
  <Text className={`text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center`}>
  {`Reseach`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center `}>
  {`Presentation`}
</Text>
</HStack>
</Box>
</Box>
  <Box>
  <Box>
  <Image src={`Image (8).svg`} sx={{"width": "384px", "height": "240px"}}/>
  <Text className={`text-sm text-[#6941C6] pb-4 pt-4`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-4`}>
  {`Our top Ten Javascript frameworks  to use`}
</Text>
  <Text className={`text-sm pb-4`}>
  {`JavaScript frameworks make development easy with extensive features and functionalities.`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center`}>
  {`Software Development`}
</Text>
  <Text className={`text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center`}>
  {`Tools`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center `}>
  {`SaaS`}
</Text>
</HStack>
</Box>
</Box>
  <Box>
  <Box>
  <Image src={`Image (9).svg`} sx={{"width": "384px", "height": "240px"}}/>
  <Text className={`text-sm text-[#6941C6] pb-4 pt-4`}>
  {`Sunday, 1 Jan 2023`}
</Text>
  <Text className={`text-xl pb-4`}>
  {`Podcast: Creating a better CX Community`}
</Text>
  <Text className={`text-sm pb-4`}>
  {`Starting a community doesn’t need to be complicated, but how do you get started?`}
</Text>
  <HStack>
  <Text className={`text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center`}>
  {`Podcast`}
</Text>
  <Text className={`text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center`}>
  {`Customer Success`}
</Text>
  <Text className={`text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center `}>
  {`Presentation`}
</Text>
</HStack>
</Box>
</Box>
</Box>
</Box>
</Fragment>
  <NextHead>
  <title>
  {`Nextpy App`}
</title>
  <meta content={`A Nextpy app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
